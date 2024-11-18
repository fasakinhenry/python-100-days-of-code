############DEBUGGING#####################

# Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# Solution
# this is quite easy to spot
# This is an indentation error and type error.
# The type error can be fixed by converting the age input to integer(type casting)
# The print statement is meant to be indented
# The IDE does a good job of pointing out the indentation error before runtime
# Here is the fix for the problem 
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}")
