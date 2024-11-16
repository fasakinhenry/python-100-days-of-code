# Calculator Project - Day 10

This project is part of the Day 10 challenge from Angela Yu's course. The goal is to build a simple calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Overview

We will create a calculator that uses functions and dictionaries to perform calculations based on user input. The calculator will continue to perform operations until the user decides to start a new calculation.

## Steps

1. Create functions for each arithmetic operation.
2. Store the functions in a dictionary.
3. Get user input for the numbers and the operation.
4. Perform the calculation using the selected operation.
5. Display the result.
6. Allow the user to continue calculating with the result or start a new calculation.

## Code Structure

- `main.py`: Contains the main logic of the calculator.
- `art.py`: Contains the ASCII art for the calculator logo.

## Usage

1. Run the `main.py` file.
2. Enter the first number.
3. Enter the second number.
4. Choose an operation from the displayed list.
5. The result will be displayed.
6. Choose to continue calculating with the result or start a new calculation.

## Example

```
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

What's the first number?: 5
What's the second number?: 10
+
-
*
/
Pick an operation from the line above: +
5.0 + 10.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: y
Pick an operation: *
What's the next number?: 3
15.0 * 3.0 = 45.0
Type 'y' to continue calculating with 45.0, or type 'n' to start a new calculation: n

 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

What's the first number?: 
```

## Tips

- Use the `input()` function to get user input.
- Use the `float()` function to convert the input to a floating-point number.
- Use the `print()` function to display the result.
- Use a dictionary to store all the operations and their respective functions.
- Use the user operation as a key to get the required operation from the operations dictionary.

## Resources

- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [Python Functions](https://www.w3schools.com/python/python_functions.asp)

## Solution

> [Check out my Solution here](./main.py)