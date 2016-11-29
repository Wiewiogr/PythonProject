import random
geneFunction = lambda : random.uniform(0,1)

class Chromosome(object):
    def __init__(self,numberOfGenes,geneInit = geneFunction):
        self.fitness = 0
        self.numberOfGenes = numberOfGenes
        self.genes = [geneInit() for x in xrange(numberOfGenes)]

if __name__ == "__main__":
    chromo = Chromosome(40)
    for x in chromo.genes:
        print x
