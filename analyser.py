import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import pylab
import pygame

def createGraph():
    fig.clf()
    ax = fig.gca()
    x = [sign*(x-25)*(x-25) for x in xrange(50)]
    ax.plot(x)
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    return renderer.tostring_rgb()

class Analyser(object):
    def __init__(self, height, width, population):
        self.height = height
        self.width = width
        self.population = population
        self.generation = -1
        self.scores = {"max": [], "average": []}
        self.figures = {"max": [], "average": [], "chromosome": []}
        self.plots = {"max": [], "average": [], "chromosome": []}
        self.figureSize = [width/2, height/2]
        self.figures["max"] = pylab.figure(figsize = [width/200, height/200] , dpi=100,)
        self.figures["average"] = pylab.figure(figsize = [width/200, height/200] , dpi=100,)
        self.figures["chromosome"] = pylab.figure(figsize = [width/100, height/200] , dpi=100,)
        #print [i*1.0/population for i in xrange(population)]
        self.plotColors = matplotlib.cm.gist_ncar([i*1.0/population for i in xrange(population)])
        #print self.plotColors

    def draw(self, screen):
        screen.fill([0,0,0])
        maxSurface = pygame.image.fromstring(self.plots["max"], self.figureSize, "RGB")
        averageSurface = pygame.image.fromstring(self.plots["average"], self.figureSize, "RGB")
        chromosomesSurface = pygame.image.fromstring(self.plots["chromosome"], [self.width,self.height/2], "RGB")
        screen.fill([255,255,255])
        screen.blit(maxSurface, (0,0))
        screen.blit(averageSurface, (self.width/2,0))
        screen.blit(chromosomesSurface, (0,10+self.height/2))

    def createGraph(self, which):
        self.figures[which].clf()
        ax = self.figures[which].gca(title=str(which+" fitness"),xlabel="generation")
        ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
        if self.generation == -1:
            ax.plot([0], '-o')
        else:
            ax.plot([i+1 for i in xrange(self.generation+1) ],self.scores[which], '-o')
        canvas = agg.FigureCanvasAgg(self.figures[which])
        canvas.draw()
        renderer = canvas.get_renderer()
        self.plots[which] = renderer.tostring_rgb()

    def createOriginList(self,chromosome):
        originList = [0 for i in xrange(self.population)]
        for gene in chromosome.genes:
            originList[gene.origin] += 1
        return originList

    def createChromosomeGraph(self, chromosomes,fitnesses):
        self.figures["chromosome"].clf()
        self.figures["chromosome"].suptitle("chromosomes genes")

        rows = (self.population / 10) + 1
        cols = self.population / rows + 1
        for i in xrange(self.population):
            self.figures["chromosome"].add_subplot(rows,cols,i+1)
            ax = self.figures["chromosome"].gca()
            ax.text(0,0,fitnesses[i], fontsize=8, verticalalignment='center', horizontalalignment='center')
            #ax.set_title(fitnesses[i], fontsize=8)
            ax.pie(self.createOriginList(chromosomes[i]), colors=self.plotColors)

        canvas = agg.FigureCanvasAgg(self.figures["chromosome"])
        canvas.draw()
        renderer = canvas.get_renderer()
        self.plots["chromosome"] = renderer.tostring_rgb()

    def update(self, fitnesses, chromosomes):
        if self.generation != -1:
            self.scores["max"].append(max(fitnesses))
            self.scores["average"].append(sum(fitnesses)/len(fitnesses))
        self.createGraph("max")
        self.createGraph("average")
        self.createChromosomeGraph(chromosomes, fitnesses)
        self.generation += 1

