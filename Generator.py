import random


def generate_grade_array(size):
    grades = []
    for i in range(0, size):
        grades.append(random.randint(1, 6))
    print("grades: ", grades)
    return grades
