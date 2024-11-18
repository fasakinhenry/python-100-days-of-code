############DEBUGGING#####################

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# By playing computer
# We can easily see the code does not include the year 1994
# Therefore when year 1994 is given, nothing is printed out
# Here is the solution
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")
