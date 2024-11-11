# Create a funtion with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    print("How are you today?")

# Call the function with postional arguments
greet_with("Henry", "London")

# Call the function with keyword arguments
greet_with(location="London", name="Henry")
