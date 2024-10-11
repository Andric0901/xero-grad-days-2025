from abc import ABCMeta, abstractmethod
from Invoice import Invoice


class TaxCalculatorInterface(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def CalculateTax(self, orders: list[Invoice]) -> dict[str, tuple[float, float]]:
        """Abstract method for calculating tax.

        Parameters:
            - orders (list[Invoice]): A list of Invoices as specified in the description

        Returns:
            - A dictionary containing the uuid (of the invoice) as the key
            and a tuple of tax rate and total, respectively
        """
        raise NotImplementedError


if __name__ == "__main__":
    pass
