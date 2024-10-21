import os
import unittest
from unittest.mock import patch
from io import StringIO

# Get the current script's directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# File paths using the current directory
testing_copy_path = os.path.join(current_directory, "testing_copy.py")
exercise_file_path = os.path.join(current_directory, "04_BMI-calculator-exercise.py")

# Step 1: Create the testing_copy.py file in the current directory
try:
    with open(exercise_file_path, "r") as original:
        with open(testing_copy_path, "w") as file:
            file.write("def test_func():\n")
            f2 = original.readlines()[0:40]
            for x in f2:
                file.write("    " + x)
except FileNotFoundError:
    print("Error: The file '04_BMI-calculator-exercise.py' could not be found. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Step 2: Now, import the module after creating the file
import sys
sys.path.append(current_directory)  # Ensure the current directory is in the system path
import testing_copy

# Step 3: Unit test implementation
class MyTest(unittest.TestCase):
    def run_test(self, given_answer, expected_print):
        with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
            testing_copy.test_func()
            self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_1(self):
        self.run_test(given_answer=['2', '8'], expected_print='2\n')

    def test_2(self):
        self.run_test(given_answer=['1.8', '85'], expected_print='26\n')

    def test_3(self):
        self.run_test(given_answer=['1.6', '90'], expected_print='35\n')


print("\n\n\n.\n.\n.")
print('Checking if you are printing a single number: \n The BMI as an integer (using meters and kilograms)...')
print('Running some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

# Clean up: Remove the testing_copy.py file after running the tests
os.remove(testing_copy_path)
