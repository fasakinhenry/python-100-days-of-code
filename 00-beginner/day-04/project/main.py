rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# Ask the user about their choice
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Create a list of choices
choices = [rock, paper, scissors]

# Get the computer's choice
computer_choice = random.randint(0, len(choices) - 1)

# Print the user's choice
print(f"You chose:\n{choices[choice]}")

# Print the computer's choice
print(f"Computer chose:\n{choices[computer_choice]}")

if choice == computer_choice:
    print("It's a draw.")
elif choice == 0 and computer_choice == 2:
    print("You win.")
elif choice == 1 and computer_choice == 0:
    print("You win.")
elif choice == 2 and computer_choice == 1:
    print("You win.")
else:
    print("You lose.")
