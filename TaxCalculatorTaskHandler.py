from TaxCalculatorInterface import TaxCalculatorInterface, CalculateTax
from Invoice import Invoice
import time


def task_calculate_tax(orders: list[Invoice], calculator: TaxCalculatorInterface):
    time.sleep(10)
    print(f"\ntask_calculate_tax Done")
    return CalculateTax(orders, calculator)


def task_break_worker(orders: list[Invoice], calculator: TaxCalculatorInterface):
    CalculateTax(orders, calculator)
    raise Exception


def task_calculate_tax_slow(orders: list[Invoice], calculator: TaxCalculatorInterface):
    time.sleep(1000000)
    print("task_calculate_tax_slow Done")
    return CalculateTax(orders, calculator)


if __name__ == "__main__":
    from Invoice import generate_invoices
    from TaxCalculatorUS import TaxCalculatorUS
    invoices = generate_invoices([1, 2, 3], num_invoices=5)
    calculator = TaxCalculatorUS()
    result = task_calculate_tax(invoices, calculator)
