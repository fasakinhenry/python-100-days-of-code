# Calculator - Part 2

In this exercise, we will extend the functionality of our calculator from Part 1. We will add the ability to continue calculations with the result of the previous calculation.

## Instructions

1. **Continue Calculations**: After performing a calculation, ask the user if they want to continue calculating with the result or start a new calculation.
2. **Recursive Function**: Use a recursive function to handle the continuation of calculations.
3. **User Input**: Prompt the user for the next operation and number if they choose to continue calculating.

## Tips

- Use the `input()` function to get user input.
- Use the `float()` function to convert the input to a floating-point number.
- Use the `print()` function to display the result.
- Use a dictionary to store all the operations and their respective functions.
- Use the user operation as a key to get the required operation from the operations dictionary.

## Example

```plaintext
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
```

## Solution

You can find the solution to this exercise [here](main.py).
