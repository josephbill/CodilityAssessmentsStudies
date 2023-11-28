# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance.

# Paste your code into this box
def calculate_balance(balance, annual_interest_rate, monthly_payment_rate):
    monthly_interest_rate = annual_interest_rate / 12.0
    
    for month in range(12):
        # Calculate minimum monthly payment
        minimum_monthly_payment = balance * monthly_payment_rate
        
        # Calculate monthly interest
        monthly_interest = balance * monthly_interest_rate
        
        # Calculate the remaining balance after the monthly payment and interest
        balance -= minimum_monthly_payment
        balance += monthly_interest
    return round(balance,2)
