# Mathematical Operations

## Introduction

In this section, we will cover basic mathematical operations in Python as taught by Angela Yu. These operations are fundamental for performing calculations and manipulating numerical data in your programs.

## Basic Operations

Python supports several basic mathematical operations:

1. **Addition (`+`)**: Adds two numbers.
    ```python
    result = 3 + 2  # result is 5
    ```

2. **Subtraction (`-`)**: Subtracts the second number from the first.
    ```python
    result = 5 - 2  # result is 3
    ```

3. **Multiplication (`*`)**: Multiplies two numbers.
    ```python
    result = 3 * 2  # result is 6
    ```

4. **Division (`/`)**: Divides the first number by the second. The result is a float.
    ```python
    result = 6 / 2  # result is 3.0
    ```

5. **Floor Division (`//`)**: Divides the first number by the second and rounds down to the nearest integer.
    ```python
    result = 7 // 2  # result is 3
    ```

6. **Modulus (`%`)**: Returns the remainder of the division of the first number by the second.
    ```python
    result = 7 % 2  # result is 1
    ```

7. **Exponentiation (`**`)**: Raises the first number to the power of the second.
    ```python
    result = 3 ** 2  # result is 9
    ```

## Order of Operations
Python follows the standard mathematical order of operations, often remembered by the acronym PEMDAS:

- **P**arentheses
- **E**xponents
- **M**ultiplication and **D**ivision (from left to right)
- **A**ddition and **S**ubtraction (from left to right)

Example:
```python
result = 3 + 2 * 2  # result is 7 because multiplication is performed before addition
result = (3 + 2) * 2  # result is 10 because parentheses are evaluated first
```
## Practical Examples
Here are some practical examples of using mathematical operations in Python:

1. Calculating the area of a rectangle:

```python
width = 5
height = 3
area = width * height  # area is 15
```

2. Converting temperature from Celsius to Fahrenheit:

```python
celsius = 25
fahrenheit = (celsius * 9/5) + 32  # fahrenheit is 77.0
```

3. Finding the remainder of a division:

```python
dividend = 10
divisor = 3
remainder = dividend % divisor  # remainder is 1
```

## Conclusion

Understanding and using mathematical operations is crucial for any programming task that involves numerical data. Practice these operations to become proficient in performing calculations in Python.

For more detailed explanations and exercises, refer to the corresponding Python scripts in the concepts directory.

