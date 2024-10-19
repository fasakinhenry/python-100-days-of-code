# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

################################
# Enter your code below this line 👇

# Check if the user input has more than two values
if len(two_digit_number) != 2:
    print("Enter a two digit number")
else:
    print(int(two_digit_number[0]) + int(two_digit_number[1]))
