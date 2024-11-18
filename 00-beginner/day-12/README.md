# Day 12 - Scope and Number Guessing game

In day 12, we learned about the scope of variables and how to create a number guessing game.

## Scope

Scope refers to the visibility of variables in a program. In Python, variables can be defined in different scopes:

- **Local Scope**: Variables defined inside a function are in the local scope. They can only be accessed within that function.
- **Global Scope**: Variables defined outside of any function are in the global scope. They can be accessed by any function in the program.
- **Block Scope**: Variables defined inside a block of code (e.g., a loop or conditional statement) are in the block scope. They can only be accessed within that block. However, Python does not have block scope in the same way as some other programming languages.

When a variable is referenced in a program, Python looks for it in the following order:

1. Local Scope
2. Enclosing Functions (if any)
3. Global Scope
4. Built-in Scope
5. If the variable is not found in any of these scopes, Python raises a `NameError`.

## Concepts

- [Namespaces - Local vs. Global Scope](./concepts/00_scope-local-and-global.py)
- [There is no block scope in Python](./concepts/01_no-block-scope.py)
- [Modifying Global Variables](./concepts/02_modify-global-scope.py)

## Project

### Number Guessing Game

We created a number guessing game with easy and hard levels. The easy level has 10 attempts to get the right number while the hard level has 5 attempts fo get the right number. For each guess, we tell the user if their guess is lower than the number. higher than the number or even equal to the number(They guessed right 😉).

- Check out the game [Here](./project/main.py)
