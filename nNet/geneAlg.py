import chromosome
import random

class GeneticAlgorithm(object):
    def __init__(self,population,crossoverRate,mutationRate,
            numberOfGenes,geneInit = chromosome.geneFunction):
        self.population = population
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
            chromo.genes[random.randint(0,chromo.numberOfGenes-1)] += 0.05
            print "mutate"


    def evolve(self):
        summedFitness = sum([x.fitness for x in self.chromosomes])
        newChromosomes = []
        while len(newChromosomes) != self.population:
            print "Before : "
            first = self.roulette(summedFitness)
            second = self.roulette(summedFitness)
            print "first fit :",first.fitness,first.genes
            print "sec fit: ",second.fitness,second.genes
            print "after :"
            self.crossover(first,second)
            print first.genes
            print second.genes
            print "mutation : "
            self.mutate(first)
            self.mutate(second)
            print first.genes
            print second.genes
            newChromosomes.append(first)
            newChromosomes.append(second)
        self.chromosomes = newChromosomes[:]
        print "number of new chromosomes",len(self.chromosomes)


if __name__ == "__main__":
    a = GeneticAlgorithm(20,0.7,0.001)
    for x in a.chromosomes:
        x.fitness = 0.5

    a.evolve(chromo)