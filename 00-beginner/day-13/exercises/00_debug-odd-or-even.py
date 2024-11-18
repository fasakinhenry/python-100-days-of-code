# Debug this code
# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Solution - Debugged code
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
# The error was in the if statement. The comparison operator should be '==' instead of '='.
  
