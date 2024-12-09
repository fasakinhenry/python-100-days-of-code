# Creating the Higher Lower game Project

# Importing the modules
from art import logo, vs
from game_data import data
import random

# Function to get the random data
def get_random_data():
    """Returns a random data from the data list"""
    return random.choice(data)

# Function to format the data
def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    # check if description starts with consonant or vowel
    if account_desc[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return f"{account_name}, an {account_desc}, from {account_country}"
    return f"{account_name}, a {account_desc}, from {account_country}"

# Function to check the answer
def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if the user is correct"""
    if a_followers > b_followers:
        return guess == 'a'
    return guess == 'b'

# Function to play the game
def play_game():
    """Function to play the Higher Lower game"""
    print(logo)
    score = 0
    game_continue = True
    account_a = get_random_data()
    account_b = get_random_data()

    while game_continue:
        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        is_correct = check_answer(guess, a_followers, b_followers)
        # Print logo
        print(logo)
        if is_correct:
            # Add a way to clear the terminal
            print("\033c")
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            # clear the screen
            print("\033c")
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False


# Calling the play_game function
play_game()
