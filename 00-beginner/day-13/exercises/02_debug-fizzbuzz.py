# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# Solution
# This is the solution
# We use and operator to check if the number is divisible by 5 and 3 instead of using or
for number in range(1, 101):
  #or should be and  
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  #if should be elif
  elif number % 3 == 0:
    print("Fizz")
  #if should be elif
  elif number % 5 == 0:
    print("Buzz")
  else:
    #This prints a list of number instead of just the number.
    print(number)
