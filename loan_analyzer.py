# coding: utf-8
import csv
from pathlib import Path
from pprint import pp


loan_costs = [500, 600, 200, 1000, 450] # sample loan costs
loan_count = len(loan_costs)
loan_sum = sum(loan_costs)
average_loan_amount = loan_sum / loan_count

print()
print("----------------------------------------")
print("Part 2: Automating the Calculations")
print()
print(f"Number of loans:        {loan_count}")
print(f"Total loan value:      ${loan_sum:.2f}")
print(f"Average loan amount:   ${average_loan_amount:.2f}")
print("----------------------------------------")


# fair value calculation for a sample loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    return future_value / (1 + annual_discount_rate/12) ** remaining_months

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
annual_discount_rate = 0.20
present_value = calculate_present_value(future_value, remaining_months, annual_discount_rate)
loan_price = loan.get("loan_price")

print()
print("----------------------------------------")
print("Part 3: Analyzing Loan Data")
print()
print(f"Future value:          ${future_value:.2f}")
print(f"Remaining months:       {remaining_months}")
print(f"Present value:         ${present_value:.2f}")
print(f"Price:                 ${loan_price:.2f}")
print()

if present_value >= loan.get("loan_price"):
    print("The present value of the loan is greater than or equal to the price.")
else:
    print("The present value of the loan is less than the cost -- it is not worth buying.")
print("----------------------------------------")


# sample loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

present_value = calculate_present_value(
    new_loan.get("future_value"), 
    new_loan.get("remaining_months"),
    annual_discount_rate=0.20
)

print()
print("----------------------------------------")
print("Part 4: Performing Financial Calculations")
print()
print(f"The present value of the new loan is: ${present_value:0.2f}")
print("----------------------------------------")


# sample loans
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

print()
print("----------------------------------------")
print("Part 5: Conditionally Filtering Lists of Loans")
print("\n")
print("The inexpensive loans are:\n")
print("--------------------")

def unsnake(s): # convert snake case to readable output
    return s.replace('_', ' ').capitalize()

for number, loan in enumerate(inexpensive_loans):
    print(f"\nLoan {number + 1}:")
    for k,v in loan.items():
        print(f"{unsnake(k):<20}{v:>20}")
    print("\n--------------------")

print("\n----------------------------------------\n")

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv")
with open(output_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    for loan in inexpensive_loans:
        w.writerow(loan.values())