############DEBUGGING#####################

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# Solution
# Problem: the code prints only 26 instead of the new list
# While using a debugger we can spot that the b_list above gets the new item appended after the end of the for loop
# Whereas at the end of the for_loop new_item is 26 which is the only value that gets appended
# If you want to print the full list, then the append line must also be in the for loop

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
