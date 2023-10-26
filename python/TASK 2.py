# Ask user to input two numbers and an operation choice-->
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

#  Now perform the calculation and display the result-->
if operation == '+':
    result = num1 + num2
    print("Result: ", result)
elif operation == '-':
    result = num1 - num2
    print("Result: ", result)
elif operation == '*':
    result = num1 * num2
    print("Result: ", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")