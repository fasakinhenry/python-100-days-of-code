from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikatu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
