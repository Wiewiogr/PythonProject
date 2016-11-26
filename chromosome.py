import random
defaultGeneFunction = lambda : random.uniform(-1,1)

class Chromosome(object):
    def __init__(self,numberOfGenes,randomGeneFunction = defaultGeneFunction):
        self.fitness = 0
        self.numberOfGenes = numberOfGenes
        self.genes = [randomGeneFunction() for x in xrange(numberOfGenes)]

if __name__ == "__main__":
    chromo = Chromosome(40)
    for x in chromo.genes:
        print x
