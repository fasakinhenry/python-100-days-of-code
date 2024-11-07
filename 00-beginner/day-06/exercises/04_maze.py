# Test out the code in the Reeborg website
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Create a function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Find the nearest available wall if there is none
while front_is_clear():
    move()
turn_left()
    
# Create the movement pattern
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
