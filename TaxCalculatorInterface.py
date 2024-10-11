from abc import abstractmethod
from Invoice import Invoice


class TaxCalculatorInterface:
    def __init__(self):
        pass

    def CalculateTax(self, orders: list[Invoice]) -> dict[str, float]:
        """Abstract method for calculating tax.

        Parameters:
            - orders (list[Invoice]): A list of Invoices as specified in the description

        Returns:
            - A dictionary containing the uuid (of the invoice) as the key
            and the total as the value.
        """
        tax_dict = {}
        for order in orders:
            tax_dict[order.uuid] = self.calculate_tax_logic(order)
        return tax_dict

    @abstractmethod
    def calculate_tax_logic(self, order: Invoice) -> float:
        raise NotImplementedError


if __name__ == "__main__":
    pass
