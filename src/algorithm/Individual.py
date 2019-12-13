import random

from .GeneticAlgorithm import is_correct


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
            prob = random.random()  # 90% szansa krzyzowania, 10% szansa mutacji
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())

        """
            Inne podejscie do krzyzowania - gorsze bo wybieramy ciagi z rodzicow, 
            a chyba lepiej zamieniac pojedyncze elementy
        
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
        cross_prob = random.random()  # 90% szansa krzyzowania, 10% szansa mutacji
        if cross_prob < 0.90:
            length = random.randint(1, len(self.chromosome) - 2)
            # length = int(len(self.chromosome) / 2)
            child_chromosome = self.chromosome[:length] + par2.chromosome[length:]
        else:
            child_chromosome = self.mutate_genes()
        """
        return Individual(child_chromosome)
