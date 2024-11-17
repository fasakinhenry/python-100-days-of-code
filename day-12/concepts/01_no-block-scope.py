# Block scope
# Python does not have any block scope unlike C++ or Java
game_level = 3

# This is perfectly valid code in Python
# The variable new_enemy is accessible outside the if block
# This is because Python does not have block scope
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)

create_enemy()
