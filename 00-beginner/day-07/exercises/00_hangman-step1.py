# Make a Hangman Game in Python using the random module.
# The game should be interactive and should have the following features:
# 1. Randomly choose a word from a list of words
# 2. Ask the user to guess a letter
# 3. Check if the letter the user guessed is one of the letters in the chosen word
# 4. If the letter is in the word, display the letter in the correct position

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter in the word: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
