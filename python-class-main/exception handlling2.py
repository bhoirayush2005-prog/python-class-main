#password validation
try:
    password = input("Enter your password: ")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    print("Password is valid.")
except ValueError as e:
    print(e)
