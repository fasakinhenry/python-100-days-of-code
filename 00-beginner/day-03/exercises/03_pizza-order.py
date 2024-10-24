# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

# Check for the user input of pizza and set bill accordingly
if size == "S":
    bill = 15
elif bill == "M":
    bill = 20
elif bill == "L":
    bill = 25

# Check if they want to add pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Check if they want to add cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
