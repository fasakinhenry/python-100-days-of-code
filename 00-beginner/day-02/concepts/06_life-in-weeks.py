# Create a life in weeks calculator according to Tim urban

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Create all the variables needed for the calculation
years_left = 90 - int(age)
weeks_left = years_left * 52
days_left = years_left * 365
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
