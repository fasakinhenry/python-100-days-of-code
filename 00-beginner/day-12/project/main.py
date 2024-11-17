# Create a number guessing game with easy and hard modes
# Import the random module
import random

# Import and print the logo
from art import logo
print(logo)

# Print the greeting message
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

# Pick a number between 1 and 100
number = random.randrange(1, 100)

# Ask for the difficulty level
should_continue = False

while not should_continue:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        should_continue = True
    elif level == "hard":
        should_continue = True
    else:
        if level != "":
            print(f" You entered {level} which is wrong. Type either 'easy' or 'hard'")
        should_continue = False

# create global attempts variable
if level == "easy":
    total_attempts = 10
else:
    total_attempts = 5

# Create a for loop to ensure user gets the correct guess withing the number of attempts
for attempt in range(total_attempts):
    remaining_attempts = total_attempts - attempt
    print(f"You have {remaining_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {guess}")
        break
    elif guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    if remaining_attempts > 1 and guess != number:
        print("Guess again.")
    else:
        print("You've run out of guesses, you lose.")
