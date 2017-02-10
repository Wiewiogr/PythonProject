from segment import Segment
from random import randint

direction = [[1,0],[0,-1],[-1,0],[0,1]]

class Snake(object):
    def __init__(self,sizeX,sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.reset()

    def reset(self):
        self.score = 0
        self.direction = randint(0,3)
        first = Segment(randint(0,self.sizeX),randint(0,self.sizeY))
        second = first + direction[self.direction]
        third = second + direction[self.direction]
        self.segments = [first, second, third]

    def rotateLeft(self):
        self.direction = (self.direction + 1) % 4

    def rotateRight(self):
        self.direction = (self.direction - 1) % 4

    def eat(self, fruitSegment):
        self.segments.append(fruitSegment)
        self.score += 1

    def move(self):
        oldSegment = self.getHead()
        newX = (oldSegment.x+direction[self.direction][0])
        if newX >= self.sizeX or newX < 0:
            return False
        newY = (oldSegment.y+direction[self.direction][1])
        if newY >= self.sizeY or newY < 0:
            return False
        newSegment = Segment(newX,newY)
        if newSegment in self.segments:
            return False
        self.segments.pop(0)
        self.segments.append(newSegment)
        return True

    def getHead(self):
        return self.segments[len(self.segments)-1]

