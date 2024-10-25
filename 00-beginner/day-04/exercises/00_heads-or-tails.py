# Write code to generate head or tail randomly
import random

sample_space = ["Heads", "Tails"]
choice = random.randint(0, 1)
print(sample_space[choice])
