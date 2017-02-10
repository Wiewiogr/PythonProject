class Segment(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, otherList):
        return Segment(self.x + otherList[0], self.y + otherList[1])

    def __sub__(self, otherList):
        return Segment(self.x - otherList[0], self.y - otherList[1])

