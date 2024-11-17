# Import the random module
import random
# Import the logo
from art import logo

# Create a function to deal cards
def deal_card():
    """Returns a new card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)

# Create a function to calculate the cards
def calculate_score(cards):
    """Takes a list of card and returns score calculated from cards"""
    if sum(cards) == 21 and len(cards) == 2:
        # Return blackjack
        return 0
    
    # Calculate the value of ace based on the sum of cards
    # ace can be either 11 or 1 depending on the total of the cards
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # Always return the sum of cards
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose, opponent has a blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over, You lose!"
    elif computer_score > 21:
        return "Opponent went over, you win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
    
def game_play():
    """Function that starts the game and handle the game play logic"""
    
    # Print the blackjack logo
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Give both user and computer two random cards each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Get the user and computer score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Print the user cards and score
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's First card: {computer_cards[0]} ")

        # Check if user has blackjack or their score is over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Check if computer score is not blackjack or greater than 21 so more cards can be added
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    game_play()
else:
    print("Goodbye!")
