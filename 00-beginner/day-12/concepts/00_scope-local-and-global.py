################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Example 2
# Local Scope
# Local scope is the scope within a function
print("Example 2 - Local Scope")

def drink_potion():
    potion_strength = 2
    print(f"The potion_strength variable defined locally is {potion_strength}")

drink_potion()
# print(potion_strength) # This will give an error

print("Example 3 - Global Scope")
# Global Scope
# Global scope is the scope outside of all functions
player_health = 10

def drink_potion():
    potion_strength = 2
    print(f"The potion_strength variable defined locally is {potion_strength}")
    print(f"player_health defined globally is : {player_health}")

drink_potion()
