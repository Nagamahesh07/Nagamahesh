#ask user for annual salary(starting salary)
annual_salary = float(input("Enter your starting annual salary: "))
house_cost = 1000000.0
down_payment = house_cost * 0.25
current_savings = 0.0
annual_return = 0.04
months = 36
semiannual_raise = 0.07

# Bisection Search Variables
epsilon = 100  # How close we need to get to the down payment
low = 0        # 0% savings
high = 10000   # 100% savings (represented as integers for precision)
steps = 0
best_saving_rate = 0.0

while True:
    steps += 1
    
    # 1.Pick the midpoint
    mid = (low + high) // 2
    rate = mid / 10000.0
    
    # 2.Reset variables for this specific rate and simulate 36 months
    current_savings = 0.0
    monthly_salary = annual_salary / 12  # Reset salary based on original input
    
    for month in range(1, months + 1):
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_salary * rate
        
        if month % 6 == 0:
            monthly_salary += monthly_salary * semiannual_raise

    # 3.Check results and update bisection bounds
    if abs(current_savings - down_payment) <= epsilon:
        best_saving_rate = rate
        break
    
    if current_savings < down_payment:
        low = mid # Saved too little,we need to save more (higher rate)
    else:
        high = mid # Saved too much,we can save less (lower rate)
        
    #If low and high meet, we can't get closer
    if low >= high - 1:
        best_saving_rate = rate # Best possible integer approximation
        break

if best_saving_rate !=0:
    print(f"Best saving rate: {best_saving_rate:.4f}")
    print(f"Steps in bisection search: {steps}")
else:
    print("It is not possible to pay the down payment in three years.")