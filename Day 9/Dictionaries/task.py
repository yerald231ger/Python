student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
    'Harry': '',
    'Ron': '',
    'Hermione': '',
    'Draco': '',
    'Neville': ''
}

for key in student_scores:
    score = student_scores[key]
    if 91 <= score <= 100:
        student_grades[key] = "Outstanding"
    if 81 <= score <= 90:
        student_grades[key] = "Exceeds Expectations"
    if 71 <= score <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

for key in student_grades:
    print(f"{key}: {student_grades[key]}")