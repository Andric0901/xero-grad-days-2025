"""..."""
import random
import uuid


class Invoice:
    def __init__(self, amount: float, tax_rate: float) -> None:
        self.amount = amount
        self.tax_rate = tax_rate
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f"Invoice uuid: {self.uuid}, Amount: {self.amount}, Tax Rate: {self.tax_rate}"


def generate_invoices(tax_rate_list: list[float] = None,
                      num_invoices: int = 10,
                      amount: int = 100) -> list[Invoice]:
    if tax_rate_list is None:
        tax_rate_list = [1, 2, 3]
    generated_list = []
    for _ in range(num_invoices):
        random_amount = amount
        random_tax_rate = random.choice(tax_rate_list)
        new_invoice = Invoice(random_amount, random_tax_rate)
        generated_list.append(new_invoice)
    return generated_list


if __name__ == "__main__":
    from pprint import pprint
    invoices = generate_invoices([5, 7, 10, 13])
    pprint(invoices)
