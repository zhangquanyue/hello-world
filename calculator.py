#!/usr/bin/env python3
import sys
Wages = int(sys.argv[1])

if __name__ == '__main__':
    taxable_income = Wages - 3500
    if 0 < taxable_income < 1500:
        tax_rate = 0.03
        tax_amount_payable = taxable_income * tax_rate - 0
        print(format(tax_amount_payable,".2f"))
    else:
        print("abc")
"""
    elif (1500  <= taxable_income < 4500):
        print("caculating…")
    elif Wages >= 4500 and < 9000:
        print('caculating…')
    elif Wages >= 9000 and < 35000:
        print('caculating')
    elif Wages >= 35000 and < 55000:
        pringt('caculating')
    elif Wages >= 55000 and < 80000:
        tax_rate = 0.35
        taxable_income = Wages - 3500
        tax_amount_payable = taxable_income * tax_rate -5505
        print(tax_amount_payable)
    elif Wages > 80000:
        tax_rate = 0.45
        taxable_income = Wages - 3500
        tax_amount_payable = taxable_income * tax_rate - 13505 
    else:
        print("低于起征点，努力赚钱哦")
"""
