#one clock for multiple exceptions
balance = 1000.0

try:
    amount = float(input("Enter the amount: "))
    if amount < 0:
        raise ValueError("amount cannot be negative.")
    if amount > balance:
        raise ValueError("Insufficient balance.") 
    else:
        balance -= amount
    print("withdrawal successful.")
    print("remaining balance:", balance)
except ValueError as e:
    print(e)
finally:
    print("Execution completed thank you for visiting.")