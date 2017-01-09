import snake, fruit

class Board(object):
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.fruit = fruit.Fruit(sizeX, sizeY)
        self.snake = snake.Snake(sizeX,sizeY)

    def update(self):
        if self.snake.getHead() == self.fruit.segment:
            self.snake.eat(self.fruit.segment)
            self.fruit.new()
            print "jemy!!"
        else:
            self.snake.move()
