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

#size = [400,400]

class Analyser(object):
    def __init__(self, height, width, population):
        self.height = height
        self.width = width
        self.scores = {"max": [1,6,3], "average": [21,5,6]}
        self.figures = {"max": [], "average": []}
        self.plots = {"max": [], "average": []}
        self.chromosomes = []
        self.figureSize = [width/2, height/2]
        self.figures["max"] = pylab.figure(figsize = [width/200, height/200] , dpi=100,)
        self.figures["average"] = pylab.figure(figsize = [width/200, height/200] , dpi=100,)

    def draw(self, screen):
        screen.fill([0,0,0])
        maxSurface = pygame.image.fromstring(self.plots["max"], self.figureSize, "RGB")
        averageSurface = pygame.image.fromstring(self.plots["average"], self.figureSize, "RGB")
        screen.fill([255,255,255])
        screen.blit(maxSurface, (0,0))
        screen.blit(averageSurface, (self.width-600,0))

    def createGraph(self, which):
        self.figures[which].clf()
        ax = self.figures[which].gca()
        ax.plot(self.scores[which])
        canvas = agg.FigureCanvasAgg(self.figures[which])
        canvas.draw()
        renderer = canvas.get_renderer()
        self.plots[which] = renderer.tostring_rgb()

    def update(self):
        self.createGraph("max")
        self.createGraph("average")


