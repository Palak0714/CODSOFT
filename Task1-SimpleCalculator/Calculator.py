# Simple Calculator in Python


# Function to perform calculation
def calculator(num1, num2, operation):
    
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Taking user input
try:
    print("-" * 50)
    print(" " * 18 + "Smart Calculator")
    print("-" * 50)
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    op = input("Enter an operation (+, -, *, /): ")

   
    # Performing calculation
    result = calculator(number1, number2, op)

   
    # Displaying result
    print("Result:", result)


except ValueError:
    print("Invalid input. Please enter numeric values.")