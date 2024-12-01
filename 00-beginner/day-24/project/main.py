#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "./input/Names/invited_names.txt")

with open(file_path, mode="r") as file:
    # Get each names without the newline character
    names = file.readlines()
    start_path = os.path.join(script_dir, "./input/Letters/starting_letter.txt")
    for name in names:
        with open(start_path, mode="r") as file:
            letter = file.read()
            final_path = os.path.join(script_dir, f"./output/ReadyToSend/letter_for_{name.strip()}.txt")
            with open(final_path, mode="w") as file:
                file.write(letter.replace("[name]", name.strip()))

# replace the name in the letter
# with open("./input/Letters/starting_letter.txt", mode="r") as file:
#     letter = file.read()
#     for name in names:
#         with open(f"./output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as file:
#             file.write(letter.replace("[name]", name.strip()))

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
