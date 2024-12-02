import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "weather-data.csv")

import pandas

data = pandas.read_csv(file_path)  # This is the way we interact with the CSV file using the pandas module
# The pandas module is a powerful data manipulation tool that makes working with data easier
print(data)

