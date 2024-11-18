############DEBUGGING#####################

# Describe Problem
# This code doesn't run
# This is because the range function does not include 20 so I will never be 20
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Solution
# Increase the endpoint of the range
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

