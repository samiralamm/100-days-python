# student_scores = {
#     "Harry": 88,
#     "Ron": 78,
#     "Hermione": 95,
#     "Draco": 75,
#     "Neville": 60,
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]

#     if score >= 91:
#         student_grades[student] = "Outstanding"
#     elif score >= 81:
#         student_grades[student] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)


# udemy version
student_scores = {'harry': 88, 'ron': 78, 'hermione':95, 'Draco': 75, 'nevillw':60}
# create an empty dictionary to collect the new values.
student_grades = {}
# loop through each key in the student_scores dictionary
for student in student_scores:
    # get the value (student score) by using the key each time.
    score = student_scores[student]
    # check what grades the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'outstanding'
    elif score >= 81:
        student_grades[student] = 'exceeds expectations'
    elif score >= 71:
        student_grades[student] = 'acceptable'
    else:
        student_grades[student] = 'fail'
print(student_grades)