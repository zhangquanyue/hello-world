#!/usr/bin/env python3
import sys
Wages = int(sys.argv[1])

if __name__ == '__main__':
    taxable_income = Wages - 3500
    if 0 < taxable_income < 1500:
        tax_rate = 0.03
        tax_amount_payable = taxable_income * tax_rate - 0
        print(format(tax_amount_payable,".2f"))
    elif 1500 <= taxable_income < 4500:
        tax_rate = 0.10
        tax_amount_payable = taxable_income * tax_rate - 105
        print(format(tax_amount_payable,".2f"))
    elif 4500 <= taxable_income < 9000:
        tax_rate = 0.20
        tax_amount_payable = taxable_income * tax_rate - 555
        print(format(tax_amount_payable,".2f"))
    elif 9000 <= taxable_income < 35000:
        tax_rate = 0.25
        tax_amount_payable = taxable_income * tax_rate - 1005
        print(format(tax_amount_payable,".2f"))
    elif 35000 <= taxable_income < 55000:
        tax_rate = 0.30
        tax_amount_payable = taxable_income * tax_rate - 2755
        print(format(tax_amount_payable,".2f"))
    elif 55000 <= taxable_income < 80000:
        tax_rate = 0.35
        tax_amount_payable = taxable_income * tax_rate -5505
        print(format(tax_amount_payable,".2f"))
    elif taxable_income >= 80000:
        tax_rate = 0.45
        tax_amount_payable = taxable_income * tax_rate -13505
        print(format(tax_amount_payable,".2f"))
    else:
        print("低于起征点，努力加油哦")
