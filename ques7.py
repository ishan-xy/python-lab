# 7. This project involves analysing the marks of students across multiple subjects. The goal is 
# to generate and analyse data, including calculating total marks, average marks, subject-wise 
# performance, and identifying top and bottom performers. You will also determine the passing 
# percentage and generate insights based on students' performance. 
# The data is an example, generate random data for the same.
# Student Name Math Physics Chemistry English 
# Arin 85 78 92 88 
# Aditya 79 82 74 90 
# Chirag 90 85 89 92 
# Gurleen 66 75 80 78 
# Kunal 70 68 75 85 

# use numpy
import numpy as np

students = ['Arin', 'Aditya', 'Chirag', 'Gurleen', 'Kunal']
math = [85, 79, 90, 66, 70]
physics = [78, 82, 85, 75, 68]
chemistry = [92, 74, 89, 80, 75]
english = [88, 90, 92, 78, 85]

marks = np.array([math, physics, chemistry, english])

total_marks = np.sum(marks, axis=0)
average_marks = np.mean(marks, axis=0)
subject_wise_performance = np.sum(marks, axis=1)
top_performers = np.argmax(total_marks)
bottom_performers = np.argmin(total_marks)
passing_percentage = np.sum(total_marks >= 40) / len(total_marks) * 100

print('Total Marks:', total_marks)
print('Average Marks:', average_marks)
print('Subject-wise Performance:', subject_wise_performance)
print('Top Performer:', students[top_performers])
print('Bottom Performer:', students[bottom_performers])
print('Passing Percentage:', passing_percentage)


