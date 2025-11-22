try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print(f"The result of {a} divided by {b} is {result}")
except ZeroDivisionError:
    print("Infinite")
    print("Error: Division by zero is not allowed.")
