from TaxCalculatorNZ import TaxCalculatorNZ
from TaxCalculatorUS import TaxCalculatorUS
from TaxCalculatorCA import TaxCalculatorCA
from Invoice import generate_invoices


def main():
    nz_invoices = generate_invoices([1, 2, 3])
    ca_invoices = generate_invoices([4, 5, 6])
    us_invoices = generate_invoices([7, 8, 9])

    calculator_nz = TaxCalculatorNZ()
    calculator_ca = TaxCalculatorCA()
    calculator_us = TaxCalculatorUS()

    result_nz = calculator_nz.CalculateTax(nz_invoices)
    result_ca = calculator_ca.CalculateTax(ca_invoices)
    result_us = calculator_us.CalculateTax(us_invoices)

    return result_nz, result_ca, result_us


if __name__ == "__main__":
    result = main()
    print(f"result_nz: {result[0]}")
    print(f"result_ca: {result[1]}")
    print(f"result_us: {result[2]}")
