class Segment(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if type(other) == list:
            return Segment(self.x + other[0], self.y + other[1])
        elif type(other) == Segment:
            return Segment(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        if type(other) == list:
            return Segment(self.x - other[0], self.y - other[1])
        elif type(other) == Segment:
            return Segment(self.x - other.x, self.y - other.y)

