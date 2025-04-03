
from random import randint
import pandas

stringss = "Hello, World!"
new_strings = [letter for letter in stringss.split()]
print(new_strings)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = { student: randint(0, 100) for student in names }
print(students_scores)

passed_students = { student: score for (student, score) in students_scores.items() if score >= 60 }
print(passed_students)

numbers = [1, 2, 3, 4, 5]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
letters = [letter for letter in name]
print(letters)

tuple = (1, 2, 3, 4, 5)
new_tuple = [n * 2 for n in tuple]
print(new_tuple)

double_numbers = [n * 2 for n in range(1, 5)]
print(double_numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [sn for sn in names if len(sn) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

duplicated_numbers = [n for n in double_numbers if n in numbers]
print(duplicated_numbers)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

my_students = {
    "name": ["Alex", "Beth", "Caroline"],
    "score": [56, 76, 98]
}
students_scores_frame = pandas.DataFrame(my_students)
print(students_scores_frame)

for (index, row) in students_scores_frame.iterrows():
    print(row.name)
    print(row.score)
