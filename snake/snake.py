from segment import Segment
from random import randint

direction = [[1,0],[0,-1],[-1,0],[0,1]]

class Snake(object):
    def __init__(self,sizeX,sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.segments = [Segment(randint(0,sizeX),randint(0,sizeY))]
        self.direction = randint(0,3)

    def rotateLeft(self):
        self.direction = (self.direction + 1) % 4

    def rotateRight(self):
        self.direction = (self.direction - 1) % 4

    def eat(self, fruitSegment):
        self.segments.append(fruitSegment)

    def move(self):
        oldSegment = self.getHead()
        newX = (oldSegment.x+direction[self.direction][0]) % self.sizeX
        newY = (oldSegment.y+direction[self.direction][1]) % self.sizeY
        newSegment = Segment(newX,newY)
        for segment in self.segments:
            if segment == newSegment:
                print "jem sie"
        self.segments.pop(0)
        self.segments.append(newSegment)

    def getHead(self):
        return self.segments[len(self.segments)-1]

