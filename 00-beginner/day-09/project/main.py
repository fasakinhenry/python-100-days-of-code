# Import the logo icon
from art import logo

# Greeting message
print(logo)
print("Welcome to the secret auction program")
# Get input from the users
name = input("What is your name?: ")
#  Get the bid amount from the user
bid = int(input("What's your bid?: $"))
# Create an empty dictionary to store the bidders
bidders = dict()

# Add the name and bid to the dictionary
bidders[name] = bid

# Ask if there are other bidders
other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

# Check if there are other bidders
while other_bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

# Find the highest bidder
highest_bid = 0
winner = ""

for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        winner = bidder

# Print the winner
print(f"The winner is {winner} with a bid of ${highest_bid}")