from abc import abstractmethod
from Invoice import Invoice


class TaxCalculatorInterface:
    def __init__(self):
        self.name = "Interface"

    @abstractmethod
    def calculate_tax_logic(self, order: Invoice) -> float:
        raise NotImplementedError


def CalculateTax(orders: list[Invoice], calculator: TaxCalculatorInterface) -> dict[str, float]:
    """A function to calculate tax.

    This function uses polymorphism, thus param "calculator" must implement
    calculate_tax_logic function.

    Parameters:
        - orders (list[Invoice]): A list of Invoices as specified in the description
        - calculator (TaxCalculatorInterface): An instantiation of TaxCalculatorInterface

    Returns:
        - A dictionary containing the uuid (of the invoice) as the key
        and the total as the value.
    """
    tax_dict = {}
    for order in orders:
        tax_dict[order.uuid] = calculator.calculate_tax_logic(order)
    return tax_dict


if __name__ == "__main__":
    pass
