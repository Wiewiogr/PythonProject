import neuralNet,chromosome,geneAlg

class Controller(object):
    def __init__(self,population,numOfInputs,numOfOutputs,
            numOfHiddenLayers,neuronsPerHiddenLayer,
            crossoverRate,mutationRate,
            geneInit = chromosome.geneFunction):
        self.population = population
        self.generation = 1
        self.chromosomeLength = (neuronsPerHiddenLayer+1)*numOfInputs
        self.chromosomeLength = neuronsPerHiddenLayer*(numOfOutputs+1)
        for i in xrange(1,numOfHiddenLayers):
            self.chromosomeLength += neuronsPerHiddenLayer*(neuronsPerHiddenLayer+1)
        self.geneticAlg = geneAlg.GeneticAlgorithm(population,
                crossoverRate,mutationRate,self.chromosomeLength,geneInit)
        self.neuralNets = [neuralNet.NeuralNet(numOfInputs,numOfOutputs,
            numOfHiddenLayers,neuronsPerHiddenLayer) for i in range(population)]
        for nNet, chromo in zip(self.neuralNets,self.geneticAlg.chromosomes):
            nNet.putWeights(chromo.genes)

