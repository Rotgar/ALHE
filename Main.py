import operator
import random

array = list(map(int, input("Podaj ciag ocen: ").split()))

POPULATION_SIZE = 20


class Individual:
    def __init__(self, cookies):
        self.chromosome = cookies
        self.fitness = sum(cookies)
        self.is_correct = is_correct(cookies)

    @staticmethod
    def mutated_genes():
        gene = random.randint(1, 6)
        return gene

    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)


def initial_population(input_scores, population_length):
    population = []

    for _ in range(0, population_length):
        series = []
        for _ in input_scores:
            val = random.randint(1, 6)
            series.append(val)
        new_individual = Individual(series)
        population.append(new_individual)
    return population


def is_correct(series):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            if series[i] <= series[i + 1]:
                return 1
        elif array[i] < array[i + 1]:
            if series[i] >= series[i + 1]:
                return 1
    return 0


def main():
    generacja = 1
    population = initial_population(array, POPULATION_SIZE)
    # for i in population:
    #     print(i.chromosome, " - ", i.is_correct, " - ", i.fitness)
    found = False
    while not found:
        population = sorted(population, key=operator.attrgetter('is_correct', 'fitness'))
        i = population[0]
        print("Generacja: ", generacja, " Ulozenie: ", i.chromosome, " - ", i.is_correct, " - ", i.fitness)
        # print("Generacja: ", generacja)

        # for i in population:
        #     print(i.chromosome, " - ", i.is_correct, " - ", i.fitness)
        new_generation = []

        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:int(POPULATION_SIZE / 2)])
            parent2 = random.choice(population[:int(POPULATION_SIZE / 2)])
            child = parent1.mate(parent2)
            new_generation.append(child)
        population = new_generation

        generacja += 1
        if population[0].fitness == 9:
            break


main()
