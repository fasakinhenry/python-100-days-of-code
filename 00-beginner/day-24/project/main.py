#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "./input/Names/invited_names.txt")

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
with open(file_path, mode="r") as file:
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    # Get each names without the newline character
    names = file.readlines()
    start_path = os.path.join(script_dir, "./input/Letters/starting_letter.txt")
    for name in names:
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        with open(start_path, mode="r") as file:
            letter = file.read()
            final_path = os.path.join(script_dir, f"./output/ReadyToSend/letter_for_{name.strip()}.txt")
            with open(final_path, mode="w") as file:
                file.write(letter.replace("[name]", name.strip()))

