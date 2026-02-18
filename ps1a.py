# Get user input for annual salary
annual_salary = float(input("Enter your annual salary: "))
# Get user input for portion of salary to save, cost of dream home
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
down_payment = total_cost * 0.25
current_savings = 0.0
annual_return = 0.04
months = 0
while current_savings < down_payment:
    # Add monthly return investment
    current_savings += (current_savings * annual_return) / 12 
    # Add monthly savings
    current_savings += (annual_salary * portion_saved) / 12
     # Increment month count 
    months += 1
# Output the number of months needed to save for the down payment
print("Number of months:", months) 
