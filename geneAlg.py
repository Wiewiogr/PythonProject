import chromosome
import random

class GeneticAlgorithm(object):
    def __init__(self,crossoverRate,mutationRate):
        self.generation = 0
        self.crossoverRate = crossoverRate
        self.mutationRate = mutationRate

    def roulette(self,chromosomes,summedFitness):
        counter = 0
        target = random.uniform(0,summedFitness)
        for chromo in chromosomes:
            counter += chromo.fitness
            if target < counter:
                return chromo

    def crossover(self,first,second):
        if random.uniform(0,self.crossoverRate):
            place = random.randint(1,first.numberOfGenes)
            first.genes[place:],second.genes[place:]=second.genes[place:],first.genes[place:]
            print "crossover"

    def mutate(self,chromo):
        if random.uniform(0,1) < self.mutationRate:
            chromo.genes[random.randint(0,chromo.numberOfGenes)] += 0.05
            print "mutate"


    def evolve(self,chromosomes):
        summedFitness = sum([x.fitness for x in chromosomes])
        first = self.roulette(chromosomes,summedFitness)
        second = self.roulette(chromosomes,summedFitness)
        self.crossover(first,second)
        self.mutate(first)
        self.mutate(second)
        self.generation += 1


if __name__ == "__main__":
    a = GeneticAlgorithm(0.7,0.001)
    chromo = [chromosome.Chromosome(20) for x in range(10)]
    for x in chromo:
        x.fitness = 0.5

    a.evolve(chromo)
