import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "weather-data.csv")

# This is the way we would normally interact with the CSV file
with open(file_path) as data_file:
    data = data_file.readlines()
    print(data)
