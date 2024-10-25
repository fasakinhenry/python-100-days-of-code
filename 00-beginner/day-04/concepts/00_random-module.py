# Implement Random numbers in python 
import random

# Print a random integer
random_integer = random.randint(1, 10)
print(random_integer)

# Print a random float betweeon 0 and 5
random_float = random.random() * 5
print(random_float)

# Usage of the random module
# Generate a random love score
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
