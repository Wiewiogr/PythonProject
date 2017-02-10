import random, gene

geneFunction = lambda : random.uniform(-1,1)

class Chromosome(object):
    def __init__(self,numberOfGenes,origin, geneInit = geneFunction):
        self.numberOfGenes = numberOfGenes
        self.genes = [gene.Gene(geneInit(),origin) for x in xrange(numberOfGenes)]

if __name__ == "__main__":
    chromo = Chromosome(40)
    for x in chromo.genes:
        print x
