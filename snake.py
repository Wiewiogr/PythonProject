#!/usr/bin/python
import sys, pygame, snake.board, nNet.controller, analyser.analyser, renderer
import numpy as np
pygame.init()

grid = 40
sizeX, sizeY = 30,15
width, height = grid*sizeX, grid*sizeY + 100
screen = pygame.display.set_mode([width,height])
gridSize = int(width/grid), int(height/grid)
board = snake.board.Board(sizeX,sizeY)

movesUntilStop = 500
population = 40
controller = nNet.controller.Controller(population,2,1,2,4,0.7,0.1)
trained = 0
fitness = []

analyser = analyser.analyser.Analyser(height, width, population)
analyser.update([0 for i in xrange(population+1)], controller.geneticAlg.chromosomes)

def draw():
    colors = [[0,100,200],[200,100,0]]
    for segment in board.snake.segments:
        pygame.draw.rect(screen,colors[0],pygame.Rect(segment.x*grid,segment.y*grid+80,grid,grid))
    pygame.draw.rect(screen,colors[1],pygame.Rect(board.fruit.x*grid,board.fruit.y*grid+80,grid,grid))

drawAll = renderer.createDrawAllFunction(draw, width, height)

def getInput():
    xFoodLocation =  np.sign(board.fruit.x - board.snake.getHead().x)
    yFoodLocation = np.sign(board.fruit.y - board.snake.getHead().y)
    surrounding = [0,0,0]

    left = board.snake.getHead() + snake.board.snake.direction[(board.snake.direction - 1)%4]
    right = board.snake.getHead() + snake.board.snake.direction[(board.snake.direction + 1)%4]
    forward = board.snake.getHead() + snake.board.snake.direction[board.snake.direction]

    if left.x < 0 or left.x >= sizeX or left.y < 0 or left.y >= sizeY:
        surrounding[0] = -1
    elif left == board.fruit.segment:
        surrounding[0] = 1

    if right.x < 0 or right.x >= sizeX or right.y < 0 or right.y >= sizeY:
        surrounding[1] = -1
    elif right == board.fruit.segment:
        surrounding[1] = 1

    if forward.x < 0 or forward.x >= sizeX or forward.y < 0 or forward.y >= sizeY:
        surrounding[2] = -1
    elif forward == board.fruit.segment:
        surrounding[2] = 1

    result = [xFoodLocation, yFoodLocation]
    result.extend(surrounding)
    return result

def moveSnake():
    _in = getInput()
    _out = controller.getOutput(_in,trained)
    print "input :", _in, "output :", _out
    choice = _out[0]
    if choice < 0.33:
        board.snake.rotateLeft()
    elif choice > 0.66:
        board.snake.rotateRight()

clock = pygame.time.Clock()
moves = movesUntilStop
fast = True
mode = "run"

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board.snake.rotateLeft()
            elif event.key == pygame.K_RIGHT:
                board.snake.rotateRight()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                fast = not fast
            elif event.key == pygame.K_a:
                if mode == "run":
                    mode = "analyse"
                else:
                    mode = "run"

    if mode == "run":
        moveSnake()

        moves -= 1
        if board.update() == False or moves == 0:
            trained += 1
            score = board.snake.score
            if score == 0:
                score = 0.15
            fitness.append(score)
            board.reset()
            moves = movesUntilStop
            if population == trained:
                controller.evolve(fitness)
                analyser.update(fitness, controller.geneticAlg.chromosomes)
                fitness = []
                trained = 0

        drawAll(screen, trained, controller.generation, board.snake.score)
        if fast:
            clock.tick(520)
        else:
            clock.tick(5)
    elif mode == "analyse":
        analyser.draw(screen)

    pygame.display.flip()

