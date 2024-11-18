############DEBUGGING#####################

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Solution
# The problem is that we are using the equal to(==) operator for word_per_page instead of assignment(=) operator
# To fix the issue, we will print the variables pages and word per page
# We then change the equal to assignment(one equal sign)
# Printing the variables made debugging this code easier
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(f"Pages = {pages}")
print(f"Word_per_page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)
