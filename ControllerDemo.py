from Invoice import generate_invoices
from TaxCalculatorInterface import CalculateTax
from TaxCalculatorNZ import TaxCalculatorNZ
from TaxCalculatorUS import TaxCalculatorUS
from TaxCalculatorCA import TaxCalculatorCA


# Demo purposes only, real life usage will vary
def main():
    nz_invoices = generate_invoices([1, 2, 3])
    ca_invoices = generate_invoices([4, 5, 6])
    us_invoices = generate_invoices([7, 8, 9])

    calculator_nz = TaxCalculatorNZ()
    calculator_ca = TaxCalculatorCA()
    calculator_us = TaxCalculatorUS()

    # Demo for polymorphism
    result_nz = CalculateTax(nz_invoices, calculator_nz)
    result_ca = CalculateTax(ca_invoices, calculator_ca)
    result_us = CalculateTax(us_invoices, calculator_us)

    return result_nz, result_ca, result_us


if __name__ == "__main__":
    result = main()
    print(f"result_nz: {result[0]}")
    print(f"result_ca: {result[1]}")
    print(f"result_us: {result[2]}")
