#!/usr/bin/env python3
import sys
def Income(income):
    Wages = income
    shebao = Wages*0.165
    taxable_income = Wages - shebao - 3500
    if 0 < taxable_income < 1500:
        tax_rate = 0.03
        tax_amount_payable = taxable_income * tax_rate - 0
        remain = Wages - tax_amount_payable - shebao
        return remain
    elif 1500 <= taxable_income < 4500:
        tax_rate = 0.10
        tax_amount_payable = taxable_income * tax_rate - 105
        remain = Wages - tax_amount_payable - shebao
        return remain
    elif 4500 <= taxable_income < 9000:
        tax_rate = 0.20
        tax_amount_payable = taxable_income * tax_rate - 555
        remain = Wages - tax_amount_payable - shebao
        return remain
    elif 9000 <= taxable_income < 35000:
        tax_rate = 0.25
        tax_amount_payable = taxable_income * tax_rate - 1005
        remain = Wages - tax_amount_payable - shebao
        return remain
    elif 35000 <= taxable_income < 55000:
        tax_rate = 0.30
        tax_amount_payable = taxable_income * tax_rate - 2755
        remain = Wages - tax_amount_payable - shebao
        return remain
    elif 55000 <= taxable_income < 80000:
        tax_rate = 0.35
        tax_amount_payable = taxable_income * tax_rate -5505
        remain = Wages - tax_amount_payable - shebao
        return remain
    elif taxable_income >= 80000:
        tax_rate = 0.45
        tax_amount_payable = taxable_income * tax_rate -13505
        remain = Wages - tax_amount_payable - shebao
        return remain
    else:
        return income - shebao
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        employee_id, wage = arg.split(':')
        try:
            income = int(wage)
        except ValueError:
            print('Parameter Error')
        after_tax_wages = Income(income)
        print('{}:{}'.format(employee_id, after_tax_wages))
