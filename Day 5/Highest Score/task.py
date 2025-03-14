student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 300, 91, 64, 89]

# Take scores from index range 0 to 5
print(student_scores[0:5])

sum_scores = 0
for score in student_scores:
    sum_scores += score

print(f"The total sum is: {sum_scores}")

min_score = student_scores[0]
for score in student_scores[1:len(student_scores)]:
    if score < min_score:
        min_score = score

print(f"The minor score is: {min_score}")

max_score = student_scores[0]
for score in student_scores[1:len(student_scores)]:
    if score > max_score:
        max_score = score

print(f"The major score is: {max_score}")
