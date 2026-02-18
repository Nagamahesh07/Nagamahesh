#ask user for annual salary(starting salary)
annual_salary = float(input("Enter your starting annual salary: "))
#ask user for portion of salary to save, cost of dream home
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
down_payment = total_cost * 0.25
current_savings = 0.0
annual_return = 0.04
months = 0
#ask user for semiannual raise
semiannual_raise = float(input("Enter the semiannual raise, as a decimal: "))
while current_savings < down_payment:
    # Add monthly return investment
    current_savings += (current_savings * annual_return) / 12
    # Add monthly savings
    current_savings += (annual_salary * portion_saved) / 12
    # Increment month count and apply semiannual raise if needed
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semiannual_raise 
# Output the number of months needed to save for the down payment
print("Number of months:", months)
