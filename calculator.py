# Simple Calculator Program

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform calculation based on the operation
result = 0
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero!")
        exit()
else:
    print("Error: Invalid operation! Please use +, -, *, or /")
    exit()

# Print the result
print(f"{num1} {operation} {num2} = {result}")
