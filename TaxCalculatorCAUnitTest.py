from TaxCalculatorCA import TaxCalculatorCA
from Invoice import Invoice
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.amount = 10
        self.tax_rate = 5
        self.offset = 4000
        self.calculator = TaxCalculatorCA()

    def test_calculate_tax_logic_canada(self):
        random_invoice = Invoice(amount=self.amount, tax_rate=self.tax_rate)
        expected = self.amount * self.tax_rate + self.amount + self.offset
        actual = self.calculator.calculate_tax_logic(random_invoice)
        try:
            assert expected == actual
        except AssertionError:
            print(f"Expected: {expected}, actual: {actual}")
            raise AssertionError


if __name__ == '__main__':
    unittest.main()
