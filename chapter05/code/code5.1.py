# code5.1.py

# Create an if, elif, else statement that displays a student's grade
# The grading scale is the 10 point scale that we use at A-B Tech. 
# For instance a score of 90 is an A, while a score of 89 is a B.
# The grades are A - F

# Get the student's score as input
score = 90

# Classify the grade based on the score
if score <= 59:
    grade = 'F'
elif score <= 69:
    grade = 'D'
elif score <= 79:
    grade = 'C'
elif score <= 89:
    grade = 'B'
else:
    grade = 'A'

# Display the grade
print(f"The student's grade is: {grade}")
