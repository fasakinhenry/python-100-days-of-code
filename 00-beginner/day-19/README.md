# Day 19 - Instances, State, and Higher-Order Functions

Welcome to Day 19 of the **Python 100 Days of Code**! Today, we will dive into **Instances**, **State**, and **Higher-Order Functions**. Additionally, we will explore **event-driven programming** and use the `turtle` module to create interactive projects that involve user input.

## Concepts

1. Instances and State
   - Understand how objects in Python maintain their **state** through attributes.
   - Learn to create and manage instances of a class.
   - Explore how changes to an instance's attributes reflect its current state.

2. Higher-Order Functions
   - Learn what makes a function a **higher-order function**.
   - Understand how to pass functions as arguments and return them from other functions.

3. Event-Driven Programming
   - Discover how event listeners allow programs to respond dynamically to user actions.
   - Use Python's `turtle` module to implement events like mouse clicks and keyboard presses.

- [Learn about Event listeners](./concepts/00_event-listeners.py)
- [Understand the turtle coordinates system](./concepts/01_understand-turtle-coordinates.py)

## Exercises

- [Create the etch a sketch app](./exercises/00_etch-a-sketch-app.py)

## Quiz

- [Check out the Quiz about turtle coordinate in HTML format here](./quiz/00_turtle-coordinate-system-quiz.html)

## Project: Turtle Racing Game

### Objective
Build a **Turtle Racing Game** where users bet on which turtle will win a race. The game should include:
- A **betting system** where the user selects a turtle by color.
- Randomized turtle movement to make the race dynamic.
- A clear finish line and an announcement of the winner.

### Features
- Multiple turtles, each with a unique color.
- User input to place bets on the winning turtle.
- A race loop that ends when a turtle crosses the finish line.
- Feedback to let the user know if their bet was correct.

### Tips for Building the Project
- Use arrays to store turtle objects, positions, and colors for easy management.
- Implement modular code to separate tasks like turtle creation, race control, and user input handling.
- Test your program with different race conditions to ensure it works smoothly.

## Project Solution

- [Turtle Racing Game Instructions](./project/instruction.md)
- [Turtle Racing Game](./project/main.py)
