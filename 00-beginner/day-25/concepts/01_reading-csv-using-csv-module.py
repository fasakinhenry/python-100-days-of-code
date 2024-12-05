import os
# import the csv module used to work with CSV files
import csv

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "weather-data.csv")

# create an array for all temperatures in weather.csv
with open(file_path) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperature = int(row[1])
            temperatures.append(temperature)
print(temperatures)
