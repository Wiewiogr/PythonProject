from segment import Segment
from random import randint

class Fruit(object):
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.segment = Segment(randint(0,sizeX-1),randint(0,sizeY-1))

    @property
    def x(self):
        return self.segment.x

    @property
    def y(self):
        return self.segment.y

    def new(self):
        self.segment = Segment(randint(0,self.sizeX-1),randint(0,self.sizeY-1))

