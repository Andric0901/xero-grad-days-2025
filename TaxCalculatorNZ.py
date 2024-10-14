# Invoice import is only for type annotation, technically not needed
from Invoice import Invoice
from TaxCalculatorInterface import TaxCalculatorInterface


class TaxCalculatorNZ(TaxCalculatorInterface):
    def __init__(self):
        super().__init__()

    def calculate_tax_logic(self, order: Invoice) -> float:
        return order.amount * order.tax_rate + order.amount + 1000
