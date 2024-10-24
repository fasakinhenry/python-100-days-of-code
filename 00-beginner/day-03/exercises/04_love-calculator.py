# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Implement the love calculator
# Count the number of times the letters in the word TRUE occurs
name1 = name1.lower()
name2 = name2.lower()
name = name1 + name2

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

first_digit = sum([t, r, u, e])
second_digit = sum([l, o, v, e])

# Combine the two digits to get the love score
love_score = int(str(first_digit) + str(second_digit))

# Print statements based on the love score
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

