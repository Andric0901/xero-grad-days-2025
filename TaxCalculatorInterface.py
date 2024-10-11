from abc import ABCMeta, abstractmethod


class TaxCalculatorInterface(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def CalculateTax(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass
