# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Attempt 1
'''
Finished the task and found out i had to use for loop so i did it again.

students = len(student_heights) #Used length function to check how many inputs or "heights" there were.
total = sum(student_heights) #I added them all together in one variable.
average_height = round(total / students) #I took the total amount from all heights and divided them on the total amount of students then rounded off the number.
print(average_height)
'''
#Attempt 2

'''
Finished the task again and did it wrong again :)

for item in student_heights:
    amount_of_students = len(student_heights)#lenght of list, how many items in the list
    total_height = sum(student_heights) #the total sum of all values in student heights
print(round(total_height / amount_of_students)) #total sum divided on the amount, rounded number and printed outside of the for loop.
'''
#Attempt 3

total_height = 0
for height in student_heights:
    total_height += height
    
total_students = 0
for students in student_heights:
    #total_students = len(student_heights)
    total_students += 1          
print(round(total_height / total_students))
