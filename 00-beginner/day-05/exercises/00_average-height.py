# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0

# Calculate the total height of all students without sum
for height in student_heights:
  total_height += height

# Calculate the number of students without len
number_of_students = 0

for student in student_heights:
  number_of_students += 1

# Calculate the average height to the nearest whole number
average_height = round(total_height / number_of_students)

# Print the average height
print(average_height)
