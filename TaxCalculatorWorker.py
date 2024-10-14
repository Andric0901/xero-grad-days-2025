import time
import random
from threading import Thread
from queue import Queue
from Invoice import Invoice
from TaxCalculatorInterface import TaxCalculatorInterface
from Invoice import generate_invoices
from TaxCalculatorNZ import TaxCalculatorNZ
from TaxCalculatorUS import TaxCalculatorUS
from TaxCalculatorCA import TaxCalculatorCA
import TaxCalculatorTaskHandler

from logtail import LogtailHandler
import logging
import os
from dotenv import load_dotenv

load_dotenv()

handler = LogtailHandler(source_token=os.getenv('SOURCE_TOKEN'))
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.handlers = []
logger.addHandler(handler)

STATUS_WORKING = "working"
STATUS_BROKEN = "broken"
STATUS_IDLE = "idle"


class TaxCalculatorWorker(Thread):
    def __init__(self, task_queue: Queue, worker_id: int):
        Thread.__init__(self)
        self.task_handler = TaxCalculatorTaskHandler  # Task handler module that has task funcs
        self.task_queue = task_queue
        self.running = True
        self.worker_id = worker_id
        self.status = STATUS_IDLE

    def run(self):
        while self.running:
            try:
                # Wait for a task indefinitely if necessary
                task_data = self.task_queue.get()
                task_name = task_data[0]
                if task_name == "STOP":
                    print(f"\nStopping worker {self.worker_id}")
                    self.running = False
                else:
                    start_time = time.time()
                    orders, calculator = task_data[1], task_data[2]
                    self.status = STATUS_WORKING + f" on {task_name} {calculator.name}"
                    time.sleep(1 * self.worker_id + random.random() * 5)
                    # Execute the task based on the task name
                    result = self.execute_task(task_name, orders, calculator)
                    print(f"by Worker {self.worker_id}")
                    print(result)
                    self.status = STATUS_IDLE
                    self.task_queue.task_done()
                    end_time = time.time()
                    logger.info(f"Finished running task for Worker {self.worker_id}", extra={
                        "metrics": {"name": f"worker{self.worker_id}.success_running_task",
                                    "duration": end_time - start_time}
                    })
            except Exception as e:
                start_time = time.time()
                # Imitate broken worker
                self.status = STATUS_BROKEN
                print(f"\nWorker {self.worker_id} Broken")
                time.sleep(2 * self.worker_id + random.random() * 8)
                # Imitate restart
                self.status = STATUS_IDLE
                print(f"\nWorker {self.worker_id} Restarted")
                end_time = time.time()
                logger.error(f"Error running task for Worker {self.worker_id}", extra={
                    "metrics": {"name": f"worker{self.worker_id}.error_running_task",
                                "duration": end_time - start_time}
                })
                self.task_queue.task_done()

    def execute_task(self,
                     task_name: str,
                     orders: list[Invoice],
                     calculator: TaxCalculatorInterface):
        if hasattr(self.task_handler, task_name):
            func = getattr(self.task_handler, task_name)
            return func(orders, calculator)
        else:
            return f"Unknown task: {task_name}"

    def get_status(self):
        return self.status


def task_input_loop(workers: list[TaxCalculatorWorker], task_queue: Queue, num_workers: int = 4):
    default_orders = generate_invoices()
    default_calculator = TaxCalculatorNZ()
    while True:
        task = input("Enter a task (or type 'exit' to quit): ")
        if task.lower() == 'exit' or task.lower() == 'stop':
            # Add STOP signal for each worker to stop after completing current tasks
            for _ in range(num_workers):
                task_queue.put(("STOP", default_orders, default_calculator))
            break
        elif task.lower() == 'break':
            task_queue.put(("task_break_worker", default_orders, default_calculator))
        elif task.lower() == 'nz':
            nz_calculator = TaxCalculatorNZ()
            task_queue.put(("task_calculate_tax", default_orders, nz_calculator))
        elif task.lower() == 'us':
            us_calculator = TaxCalculatorUS()
            task_queue.put(("task_calculate_tax", default_orders, us_calculator))
        elif task.lower() == 'ca':
            ca_calculator = TaxCalculatorCA()
            task_queue.put(("task_calculate_tax", default_orders, ca_calculator))
        elif task.lower() == 'slow':
            task_queue.put(("task_calculate_tax_slow", default_orders, default_calculator))
        elif task.lower() == 'status':
            check_worker_status(workers)
        elif task.lower() == 'mega_break':
            for _ in range(30):
                task_queue.put(("task_break_worker", default_orders, default_calculator))
        elif task.lower() == 'mega_task':
            for _ in range(30):
                task_queue.put(("task_calculate_tax", default_orders, default_calculator))
        else:
            task_queue.put((task, default_orders, default_calculator))


def check_worker_status(workers: list[TaxCalculatorWorker]):
    for worker in workers:
        print(f"Worker {worker.worker_id} status: {worker.get_status()}")


if __name__ == "__main__":
    task_queue = Queue()
    num_workers = 4
    workers = [TaxCalculatorWorker(task_queue, worker_id) for worker_id in range(1, num_workers + 1)]
    for worker in workers:
        worker.start()
    task_input_loop(workers, task_queue, num_workers)
    task_queue.join()  # Ensure all tasks are completed
    print("All tasks processed. Exiting...")
