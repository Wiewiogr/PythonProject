import neuralNet,chromosome,geneAlg

class Controller(object):
    def __init__(self,population,numOfInputs,numOfOutputs,
            numOfHiddenLayers,neuronsPerHiddenLayer,
            crossoverRate,mutationRate,
            geneInit = chromosome.geneFunction):
        self.population = population
        self.generation = 1
        self.chromosomeLength = neuronsPerHiddenLayer*(numOfInputs+1)
        self.chromosomeLength += (neuronsPerHiddenLayer+1)*numOfOutputs
        for i in xrange(1,numOfHiddenLayers):
            self.chromosomeLength += neuronsPerHiddenLayer*(neuronsPerHiddenLayer+1)
        self.geneticAlg = geneAlg.GeneticAlgorithm(population,
                crossoverRate,mutationRate,self.chromosomeLength,geneInit)
        self.neuralNets = [neuralNet.NeuralNet(numOfInputs,numOfOutputs,
            numOfHiddenLayers,neuronsPerHiddenLayer) for i in xrange(population)]
        for nNet, chromo in zip(self.neuralNets,self.geneticAlg.chromosomes):
            nNet.putWeights(chromo.genes)

    def evolve(self,fitness):
        print "evolve :",fitness
        self.geneticAlg.fitnesses = fitness[:]
        self.generation += 1
        self.geneticAlg.evolve()
        for i in xrange(len(self.neuralNets)):
            self.neuralNets[i].putWeights(self.geneticAlg.chromosomes[i].genes)

    def getOutput(self,inputs,index):
        return self.neuralNets[index].getOutput(inputs)

