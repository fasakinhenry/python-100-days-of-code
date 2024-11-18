############DEBUGGING#####################

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Solution
# After reproducing the bug by setting dice_num to 6(dice_num = 6)
# We notice the index goes out of range in that case
# The problem is that dice_num includes both endpoints 1 and 6 so when it becomes 6 it gives an error
# Here is the solution
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# Change the endpoints of the random dice_num
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
