# import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# new_names = [name.upper() for name in names if len(name) > 4]
# print(new_names)

# num = [num for num in range(11)]
# print(num)

# student_scores = {key:random.randint(1,101) for key in names }
# print(student_scores)

# passed = {score:value for (score,value) in student_scores.items() if value > 50}
# print(passed)



#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)
