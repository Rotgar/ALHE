#
# Algorytm genetyczny
#
import operator
import random

POPULATION_SIZE = 100
INPUT_GRADE_ARRAY = []
# Sygnalizuje czy w populacji jest osobnik z poprawnym ustawieniem - jesli tak to mozna sortowac
setup_condition = False


def initial_population(input_scores, population_length):
    from .Individual import Individual
    population = []

    for _ in range(0, population_length):
        series = []
        for _ in input_scores:
            val = random.randint(1, 6)
            series.append(val)
        new_individual = Individual(series)
        population.append(new_individual)
    return population


# Funkcja porownujaca ciag 'ciastek' z lista wejsciowś w celu sprawdzenia warunku,
# czy sasiad z wieksza ocena dostal wiecej ciastek
def is_correct(series):
    global setup_condition
    for i in range(len(INPUT_GRADE_ARRAY) - 1):
        if INPUT_GRADE_ARRAY[i] > INPUT_GRADE_ARRAY[i + 1]:
            if series[i] <= series[i + 1]:
                return 1
        elif INPUT_GRADE_ARRAY[i] < INPUT_GRADE_ARRAY[i + 1]:
            if series[i] >= series[i + 1]:
                return 1
    setup_condition = True  # sygnal ze znaleziono poprawne ustawienie
    return 0  # 0 oznacza ze poprawne ustawienie, aby potem sortowac rosnaco


def print_population(population):
    for num in range(len(population)):
        ind = population[num]
        print(num, ": ", ind.chromosome, " - ", ind.is_correct, " - ", ind.fitness)


# Funkcja do przenoszenia co najzwyzej 10% najlepszych, roznych od siebie osobnikow z
# poprzedniej generacji do nowej
def select_best_for_next_generation(new_generation, actual_generation):
    kept_amount = int((10 * POPULATION_SIZE) / 100)

    counter = 0
    while (kept_amount != 0) and (counter != len(actual_generation)):
        omit = False
        for member in new_generation:
            if member.chromosome == actual_generation[counter].chromosome:
                omit = True
                break
        if not omit:
            new_generation.append(actual_generation[counter])
            kept_amount -= 1
        counter += 1


def run_genetic_algorithm(correct_result, population_size, input_grades, show_populations):
    global POPULATION_SIZE, INPUT_GRADE_ARRAY
    POPULATION_SIZE = population_size
    INPUT_GRADE_ARRAY = input_grades

    generation = 1
    population = initial_population(INPUT_GRADE_ARRAY, POPULATION_SIZE)  # inicjuje losowo poczatkowa populacje

    found_result = False
    while not found_result:

        new_generation = []

        # dopiero gdy w populacji sa osobniki z poprawnym ustawieniem, bo wiadomo ze sa najlepszymi do przenoszenia
        # i krzyzowania, a w tym celu powinny zostac umieszczone na poczatku
        if setup_condition:
            population = sorted(population, key=operator.attrgetter('is_correct', 'fitness'))
            select_best_for_next_generation(new_generation, population)

        if show_populations:
            print("Generacja: ", generation)
            print_population(population)

        remaining_population_size = int(POPULATION_SIZE - len(new_generation))
        for _ in range(remaining_population_size):
            parent1 = random.choice(population[:int(POPULATION_SIZE / 2)])  # wybiera losowego osobnika z 50% populacji
            parent2 = random.choice(population[:int(POPULATION_SIZE / 2)])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation
        generation += 1

        if (population[0].fitness == correct_result) and (population[0].is_correct == 0):
            found_result = True
    return population[0]
