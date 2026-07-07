student_scores = [80, 20,60,90,70,76,74,89,80,97,89,]
# total_exam_score = sum(student_scores)
# print(total_exam_score)
# sum = 0
# for score in student_scores:
    # sum +=  student_scores
# print(sum)

# print(max(student_scores))
max_scores = 0
for score in student_scores:
    if score > max_scores:
        max_scores = score
print(max_scores)


