from src.algorithm.ClassicAlgorithm import run_linear_algorithm
from src.algorithm.Generator import generate_grade_array
from src.algorithm.GeneticAlgorithm import run_genetic_algorithm

input_choice = input("Wybierz: \n 1: Wygeneruj losowy ciag liczb(ocen), \n [cokolwiek != 1]: Wpisz ciag recznie \n : ")
array = []

print("input: ", input_choice)

if input_choice == "1":
    size = int(input("Podaj liczbe ocen: "))
    array = generate_grade_array(size)
else:
    array = list(map(int, input("Podaj ciag ocen: ").split()))

show_populations = input("Pokazac kolejne generowane populacje?('y' - tak): ")
if show_populations == 'y':
    show_populations = True
else:
    show_populations = False

population_size = 100
try:
    population_size = int(input("Podaj liczebnosc populacji w generacji(standardowo 100): "))
except ValueError:
    population_size = 100


def main():
    result = run_linear_algorithm(array)  # zwraca poprawny wynik z algorytmu klasycznego
    print("Wynik alg klasycznego: ", result)

    result_setup = run_genetic_algorithm(result, population_size, array, show_populations)
    print("Koncowe ustawienie: \n", result_setup.chromosome, "\nPoczatkowe ustawienie: \n", array if show_populations
    else "\n", "\n Wynik: ", result_setup.fitness)


main()
