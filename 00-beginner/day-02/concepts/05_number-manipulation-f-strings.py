# Number Manipulation and F-Strings

# Basic Arithmetic Operations
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b

print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")
print(f"Floor Division: {a} // {b} = {floor_division}")
print(f"Modulus: {a} % {b} = {modulus}")
print(f"Exponentiation: {a} ** {b} = {exponentiation}")

# Rounding Numbers
number = 3.14159
rounded_number = round(number, 2)
print(f"Rounded Number: {number} rounded to 2 decimal places is {rounded_number}")

# F-Strings with Expressions
name = "Angela"
age = 30
height = 1.75

print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")

# Formatting Numbers with F-Strings
large_number = 1234567890
formatted_number = f"{large_number:,}"
print(f"Formatted Number with commas: {formatted_number}")

# Using f-strings to embed expressions
x = 5
y = 10
print(f"The sum of {x} and {y} is {x + y}.")
print(f"The product of {x} and {y} is {x * y}.")
