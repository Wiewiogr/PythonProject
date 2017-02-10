import chromosome, gene, random, copy

class GeneticAlgorithm(object):
    def __init__(self,population,crossoverRate,mutationRate,
            numberOfGenes,geneInit = chromosome.geneFunction):
        self.population = population
        self.crossoverRate = crossoverRate
        self.mutationRate = mutationRate
        self.fitnesses = []
        self.chromosomes = [chromosome.Chromosome(numberOfGenes,i,geneInit)
                for i in xrange(population)]

    def roulette(self,summedFitness):
        counter = 0
        target = random.uniform(0,summedFitness)
        for i in xrange(len(self.fitnesses)):
            counter += self.fitnesses[i]
            if target < counter:
                return self.chromosomes[i]

    def crossover(self,first,second):
        if random.uniform(0,self.crossoverRate):
            place = random.randint(1,first.numberOfGenes)
            first.genes[place:],second.genes[place:]=second.genes[place:],first.genes[place:]

    def mutate(self,chromo):
        if random.uniform(0,1) < self.mutationRate:
            choice = random.randint(0,chromo.numberOfGenes-1)
            chromo.genes[choice] = gene.Gene(chromosome.geneFunction(),chromo.genes[choice].origin)

    def evolve(self):
        summedFitness = sum(self.fitnesses)
        newChromosomes = []
        while len(newChromosomes) != self.population:
            first = copy.deepcopy(self.roulette(summedFitness))
            second = copy.deepcopy(self.roulette(summedFitness))
            self.crossover(first,second)
            self.mutate(first)
            self.mutate(second)
            newChromosomes.append(first)
            newChromosomes.append(second)
        self.chromosomes = newChromosomes[:]

if __name__ == "__main__":
    a = GeneticAlgorithm(20,0.7,0.001)
    for x in a.chromosomes:
        x.fitness = 0.5

    a.evolve(chromo)
