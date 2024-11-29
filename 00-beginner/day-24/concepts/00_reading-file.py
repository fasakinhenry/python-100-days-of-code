# There are two ways of reading from a file
# This is the first one which will be commented out
# The first one requires a file closing at the end so it can work well
file = open("./00-beginner/day-24/concepts/my_file.txt")
contents = file.read()
print(contents)
file.close()
