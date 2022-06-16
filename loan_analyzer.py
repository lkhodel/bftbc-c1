# coding: utf-8
import csv
from pathlib import Path
from pprint import pp

"""
This is challenge 1 for the UC Berkeley FinTech bootcamp. The script is a 
demonstration of automation for tasks associated with micro-loan valuation.
"""

# provided sample loan costs
loan_costs = [500, 600, 200, 1000, 450]
loan_count = len(loan_costs)
loan_sum = sum(loan_costs)
average_loan_amount = loan_sum / loan_count

print()
print(f"Number of loans:        {loan_count}")
print(f"Total loan value:      ${loan_sum:.2f}")
print(f"Average loan amount:   ${average_loan_amount:.2f}")
print()


# Fair value calculation for a sample loan
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    return future_value / (1 + annual_discount_rate/12) ** remaining_months

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
annual_discount_rate = 0.20
present_value = calculate_present_value(future_value, remaining_months, annual_discount_rate)

print(f"Future value:          ${future_value:.2f}")
print(f"Remaining months:       {remaining_months}")
print(f"Present value:         ${present_value:.2f}")

if present_value >= loan.get("loan_price"):
    print("The present value of the loan is greater than or equal to the price.")
else:
    print("The present value of the loan is less than the cost -- it is not worth buying.")
print("\n")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

present_value = format(present_value, ".2f")
print(f"The present value of the new loan is: ${present_value}")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans = []

for loan in loans:
    if loan.get("loan_price") <= 500:
        inexpensive_loans.append(loan)

print("The inexpensive loans are: ")
pp(inexpensive_loans)

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv")
with open(output_path, "w") as c:
    w = csv.writer(c)
    w.writerow(header)
    for loan in inexpensive_loans:
        w.writerow(loan.values())