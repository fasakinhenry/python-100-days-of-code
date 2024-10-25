# Create a list of states in America
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Print the first state in the list
print(states_of_america[0])

# Print the last state in the list uding negative indexing
print(states_of_america[-1])

# Change item in the list
states_of_america[1] = "Pencilvania"
print(states_of_america)

# Add item to the list
states_of_america.append("Henryland")

# Extend the list
states_of_america.extend(["Jesseland", "Henryland"])
