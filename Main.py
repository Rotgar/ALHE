import operator
import random

from ClassicAlgorithm import run_linear_algorithm

array = list(map(int, input("Podaj ciag ocen: ").split()))

POPULATION_SIZE = 100


class Individual:
    def __init__(self, cookies):
        self.chromosome = cookies
        self.fitness = sum(cookies)
        self.is_correct = is_correct(cookies)

    @staticmethod
    def mutated_genes():
        gene = random.randint(1, 6)
        return gene

    def mutate_genes(self):
        mutated_chromosome = []
        for i in range(len(self.chromosome)):
            mutate_gene_prob = random.random()
            if mutate_gene_prob < 0.50:
                mutated_chromosome.append(self.mutated_genes())
            else:
                mutated_chromosome.append(self.chromosome[i])
        return mutated_chromosome

    def mate(self, par2):
        child_chromosome = []
        # for gp1, gp2 in zip(self.chromosome, par2.chromosome):
        #     prob = random.random()  # 90% szansa krzyzowania, 10% szansa mutacji
        #     if prob < 0.45:
        #         child_chromosome.append(gp1)
        #     elif prob < 0.90:
        #         child_chromosome.append(gp2)
        #     else:
        #         child_chromosome.append(self.mutated_genes())
        #
        # return Individual(child_chromosome)
        cross_prob = random.random()  # 90% szansa krzyzowania, 10% szansa mutacji
        if cross_prob < 0.90:
            length = int(len(self.chromosome) / 2)
            child_chromosome = self.chromosome[:length] + par2.chromosome[length:]
        else:
            child_chromosome = self.mutate_genes()

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


def print_population(population):
    print("Population: ", "\n")
    for i in range(len(population)):
        print(i, ": ", population[i].chromosome)


def main():
    result = run_linear_algorithm(array)  # zwraca poprawny wynik z algorytmu klasycznego
    print("Result: ", result)

    generation = 1
    population = initial_population(array, POPULATION_SIZE)  # inicjule losowo poczatkowa populacje

    found = False
    while not found: # PROBLEM - generacja moze byc zaspamiona tymi samymi wartosciami przez co krzyzowki beda wytwarzac w kolko to samo i tak w nieskonczonosc do nieczego nie dochodzac
        # - pomaga wieksza popluacja, ale trzeba przemyslec czy nie wprowadzic np eleiminacji powtorzen jak jest za duzo
        population = sorted(population, key=operator.attrgetter('is_correct', 'fitness'))
        # print_population(population)
        i = population[0]
        print("Generacja: ", generation, " Chromosom: ", i.chromosome, " - ", i.is_correct, " - ", i.fitness)

        new_generation = []

        s = int((10 * POPULATION_SIZE) / 100)  # 10% najlepszych osobnikow przechodzi do kolejnej generacji
        new_generation.extend(population[:s])

        s = int((90 * POPULATION_SIZE) / 100)  # pozostale 90% powstaje przez krzyzowanie i mutacje
        for _ in range(s):
            parent1 = random.choice(population)  # [:int(POPULATION_SIZE / 2)])
            parent2 = random.choice(population)  # [:int(POPULATION_SIZE / 2)])
            child = parent1.mate(parent2)
            new_generation.append(child)
        population = new_generation

        generation += 1

        if (population[0].fitness == result) and (population[0].is_correct == 0):
            found = True


main()
