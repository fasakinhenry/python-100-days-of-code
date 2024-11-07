# This is the code to implement the turn around of karel the robot in reeborg world
# The link to the reeborg world where the code can be typed is:
# Copy the code below and paste it in reeborg world and run it to see the result
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_around():
    turn_left()
    turn_left()

move()
move()
turn_around()
move()
move()
turn_around()

