# Odd or Even
## Instructions

Write a program that determines whether a given number is odd or even.

Even numbers can be divided by 2 with no remainder.

For example:
- 86 is even because 86 ÷ 2 = 43, which is a whole number(has no decimal place)
- 59 is odd because 59 ÷ 2 = 29.5, which is not a whole number.

The modulo operator in Python is represented by the percentage sign (%). It gives you the remainder after a division.

Examples:
- `6 ÷ 2 = 3` with no remainder, so `6 % 2 = 0`
- `5 ÷ 2 = 2` with a remainder of 1, so `5 % 2 = 1`
- `14 ÷ 4 = 3` with a remainder of 2, so `14 % 4 = 2`

**Warning:** Your output should match the example output format exactly, including the positions of commas and full stops.

## Example Input 1

```
43
```

## Example Output 1

```
This is an odd number.
```

## Example Input 2

```
94
```

## Example Output 2

```
This is an even number.
```
## Hint

All even numbers can be divided by 2 with 0 remainder. Try using the modulo operator with some odd and even numbers to see the pattern:
- Odd numbers: `3 % 2`, `5 % 2`, `7 % 2`
- Even numbers: `4 % 2`, `6 % 2`, `8 % 2`

## Test Your Code

Before checking the solution, try copy-pasting your code into this repl:

[https://repl.it/@appbrewery/day-3-1-test-your-code](https://repl.it/@appbrewery/day-3-1-test-your-code)

This repl includes testing code that will check if your code meets this assignment's objectives.

## Solution

[https://repl.it/@appbrewery/day-3-1-solution](https://repl.it/@appbrewery/day-3-1-solution)

## Personal solution

- [odd or even number python file](./01_odd-or-even.py)
