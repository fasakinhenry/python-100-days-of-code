# Learning about modifying global scope

enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()

print(f"enemies outside function: {enemies}")

# Example 2
print("Example 2 - Avoid modifying global scope at all times")

# Avoid modifying global scope at all times
# It makes debugging difficult
# It makes code harder to understand
# It makes code harder to maintain

enemies2 = 1

def increase_enemies2():
  return enemies2 + 1

enemies2 = increase_enemies2()
print(f"enemies2 outside function: {enemies2}")
