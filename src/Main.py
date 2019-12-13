from src.algorithm.ClassicAlgorithm import run_linear_algorithm
from src.algorithm.Generator import generate_grade_array
from src.algorithm.GeneticAlgorithm import run_genetic_algorithm

show_populations = 'n'
population_size = 100
array = []


def load_user_array():
    global array
    correct = False
    while not correct:
        try:
            array = list(map(int, input("Podaj ciag ocen(cyfry od 1 do 6, oddzielone spacja): ").split()))
        except ValueError:
            print("Tylko cyfry dozwolone!")
            continue

        only_numbers = True
        for member in array:
            if member not in [1, 2, 3, 4, 5, 6]:
                print("Tylko cyfry od 1 do 6!")
                only_numbers = False
                break
        if only_numbers:
            correct = True


def init():
    global array, population_size, show_populations

    input_choice = input("Wybierz: \n 1: Wygeneruj losowy ciag liczb(ocen) \n !1: Wpisz ciag recznie\n : ")

    if input_choice == "1":
        size = int(input("Podaj liczbe ocen do wygenerowania: "))
        array = generate_grade_array(size)
    else:
        load_user_array()

    show_populations = input("Pokazac kolejne generowane populacje?('y' - tak): ")
    if show_populations == 'y':
        show_populations = True
    else:
        show_populations = False

    try:
        population_size = int(input("Podaj liczebnosc populacji w generacji(standardowo 100): "))
    except ValueError:
        population_size = 100


def main():
    init()
    result = run_linear_algorithm(array)  # zwraca poprawny wynik z algorytmu klasycznego
    print("Wynik alg klasycznego: ", result)

    result_setup = run_genetic_algorithm(result, population_size, array, show_populations)
    print("Koncowe ustawienie: \n", result_setup.chromosome, "\nPoczatkowe ustawienie: \n", array if show_populations
    else "", "\n Wynik: ", result_setup.fitness)


if __name__ == "__main__":
    main()
