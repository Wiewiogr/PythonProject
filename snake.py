import sys, pygame, snake.board, nNet.controller, analyser
import numpy as np
pygame.init()

grid = 40
sizeX, sizeY = 30,18
width, height = grid*sizeX, grid*sizeY + 80
black = 0, 0, 0
screen = pygame.display.set_mode([width,height])
gridSize = int(width/grid), int(height/grid)
font = pygame.font.Font(None,25)
board = snake.board.Board(sizeX,sizeY)

movesUntilStop = 500
population = 40
controller = nNet.controller.Controller(population,2,1,2,4,0.7,0.1)
trained = 0
fitness = []

analyser = analyser.Analyser(height, width, population)
analyser.update([0 for i in xrange(population+1)], controller.geneticAlg.chromosomes)

colors = [[0,0,0],[0,100,200],[200,100,0],[100,200,0],[230,150,18],[255,0,0],[224,23,246],[23,231,246],[255,255,0],[160,160,0]]

def drawAll():
    screen.fill(black)
    screen.blit(font.render("num "+str(trained)+" score : "+str(board.snake.score),1,(255,255,255)),[5,5])
    screen.blit(font.render("generation : "+str(controller.generation),1,(255,255,255)),[5,30])
    for segment in board.snake.segments:
        pygame.draw.rect(screen,colors[1],pygame.Rect(segment.x*grid,segment.y*grid+80,grid,grid))

    pygame.draw.rect(screen,colors[2],pygame.Rect(board.fruit.x*grid,board.fruit.y*grid+80,grid,grid))

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

def parseOutput(output):
    choice = output[0]
    if choice < 0.33:
        board.snake.rotateLeft()
    elif choice > 0.66:
        board.snake.rotateRight()

def moveSnake():
    _in = getInput()
    _out = controller.getOutput(_in,trained)
    print "input :", _in, "output :", _out
    parseOutput(_out)

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
        #moveSnake()

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

        drawAll()
        if fast:
            clock.tick(520)
        else:
            clock.tick(5)
    elif mode == "analyse":
        analyser.draw(screen)

    pygame.display.flip()

