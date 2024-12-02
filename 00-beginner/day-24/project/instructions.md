# Mail Merge challenge

The challenge is to create a mail merge program that reads a template letter and a list of names and addresses to send the letter to, then generates personalized letters for each person in the list.

## Files Provided

1. Get the input names from the `invited_names.txt` file in the `Input/Names` folder.
2. Get the template letter from the `letter_template.txt` file in the `Input/Letters` folder.
3. Get the output letters from the `ReadyToSend` folder in the `Output` folder.

## Tips

1. Use the `open()` function to read the files.
2. Use the `readlines()` method to read the contents of the files and return a list of lines(names in this case).
3. Use the `replace()` method to replace the placeholder in the template letter with the name of the person.
4. Use the `write()` method to write the personalized letter to a new file.
5. Use the `with` keyword to open the files and automatically close them when done.
6. Use a for loop to iterate over the list of names and write a personalized letter for each person.

## Project Solution

The solution to this project can be found in the `main.py` file.

- [Click here to view my solution](./main.py)

Happy coding!
