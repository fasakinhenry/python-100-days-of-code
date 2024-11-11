#Write your code below this line 👇
# Create an area Calculator for painting
def paint_calc(height, width, cover):
    area = height * width
    # Give an rounded up value for no. of cans
    number_of_cans = int(area / cover) + (area % cover > 0)
    print(f"You'll need {number_of_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
