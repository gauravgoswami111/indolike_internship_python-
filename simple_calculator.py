import math

# Function to log calculations
def log_calculation(history, expression, result):
    history.append(f"{expression} = {result}")

# Function to get valid numerical input
def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error! Invalid input for logarithm."
    return math.log(x, base)

# Main calculator function
def calculator():
    history = []
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Exponent")
        print("7. Logarithm")
        print("8. View Calculation History")
        print("9. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '9':
            print("Exiting the calculator.")
            break

        if choice == '8':
            if history:
                print("\nCalculation History:")
                for entry in history:
                    print(entry)
            else:
                print("No calculations yet.")
            continue

        if choice in ['1', '2', '3', '4']:
            num1 = get_input("Enter first number: ")
            num2 = get_input("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            log_calculation(history, f"{num1} + {num2}", result)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            log_calculation(history, f"{num1} - {num2}", result)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            log_calculation(history, f"{num1} * {num2}", result)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            log_calculation(history, f"{num1} / {num2}", result)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            num = get_input("Enter number: ")
            result = square_root(num)
            log_calculation(history, f"sqrt({num})", result)
            print(f"sqrt({num}) = {result}")
        elif choice == '6':
            num1 = get_input("Enter base: ")
            num2 = get_input("Enter exponent: ")
            result = power(num1, num2)
            log_calculation(history, f"{num1} ^ {num2}", result)
            print(f"{num1} ^ {num2} = {result}")
        elif choice == '7':
            num1 = get_input("Enter number: ")
            base = get_input("Enter base: ")
            result = logarithm(num1, base)
            log_calculation(history, f"log({num1}) base {base}", result)
            print(f"log({num1}) base {base} = {result}")
        else:
            print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()