# Calculator Part 1 - Combining Dictionaries and Functions

In this part, we are going to build the first part of our calculator project and we are going to be using dictionaries and functions.

## Overview

We will create a simple calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The operations will be stored in a dictionary, and we will use functions to perform the calculations.

## Steps

1. Create functions for each arithmetic operation.
2. Store the functions in a dictionary.
3. Get user input for the numbers and the operation.
4. Perform the calculation using the selected operation.
5. Display the result.

## Code Structure

- `main.py`: Contains the main logic of the calculator.
- `art.py`: Contains the ASCII art for the calculator logo.

## Usage

1. Run the `main.py` file.
2. Enter the first number.
3. Enter the second number.
4. Choose an operation from the displayed list.
5. The result will be displayed.

## Example

```
Enter the first number: 10
Enter the second number: 5
Choose an operation:
+
-
*
/
Operation: +
10 + 5 = 15
```

## Tips

- Use the `input()` function to get user input.
- Use the `int()` function to convert the input to an integer.
- Use the `print()` function to display the result.
- use the dictionary to store all the operations and their respective functions
- use user operation as key to get the required operation from the operations dictionary

## Resources

- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [Python Functions](https://www.w3schools.com/python/python_functions.asp)

## Solution

- [Solution](./main.py)

## Next Steps

In the next part, we will add more functionality to our calculator and improve the user experience.
