import random


def generate_grade_array(size):
    grades = []
    for i in range(size):
        grades.append(random.randint(1, 6))
    print("Wygenerowany ciag: \n", grades)
    return grades
