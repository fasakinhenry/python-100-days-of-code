# Create the python calculator project part 1
# Create all the functions that will be used in the calculator
def add(n1, n2):
    """Returns the addition of two numbers n1 and n2"""
    return n1 + n2

def subtract(n1, n2):
    """Returns the subtraction of two numbers n1 and n2"""
    return n1 - n2

def multiply(n1, n2):
    """Returns the multiplication of two numbers n1 and n2"""
    return n1 * n2

def divide(n1, n2):
    """Returns the division of two numbers n1 and n2"""
    return n1 / n2

# import logo from art
from art import logo

# Print the logo
print(logo)



# create a dictionary to store the operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Create variables to store the user numbers
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

# Create a loop to ask the user for the operation
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

# Call the operation function from the operations dictionary
calculation_function = operations[operation_symbol]
result = calculation_function(num1, num2)

# Print the result
print(f"{num1} {operation_symbol} {num2} = {result}")

# Ensure continuation of the calculator
continue_calculating = True
while continue_calculating:
    user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if user_choice == "y":
        num1 = result
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
    else:
        continue_calculating = False
        print("Goodbye")
