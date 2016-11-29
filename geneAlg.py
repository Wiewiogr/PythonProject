import chromosome
import random

class GeneticAlgorithm(object):
    def __init__(self,population,crossoverRate,mutationRate,
            numberOfGenes,geneInit = chromosome.geneFunction):
        self.generation = 0
        self.crossoverRate = crossoverRate
        self.mutationRate = mutationRate
        self.chromosomes = [chromosome.Chromosome(numberOfGenes,geneInit)
                for i in xrange(population)]

    def roulette(self,summedFitness):
        counter = 0
        target = random.uniform(0,summedFitness)
        for chromo in self.chromosomes:
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


    def evolve(self):
        summedFitness = sum([x.fitness for x in chromosomes])
        first = self.roulette(self.chromosomes,summedFitness)
        second = self.roulette(self.chromosomes,summedFitness)
        self.crossover(first,second)
        self.mutate(first)
        self.mutate(second)
        self.generation += 1


if __name__ == "__main__":
    a = GeneticAlgorithm(20,0.7,0.001)
    for x in a.chromosomes:
        x.fitness = 0.5

    a.evolve(chromo)
