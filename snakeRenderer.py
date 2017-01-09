import sys, pygame, snake.board
pygame.init()

grid = 12
sizeX, sizeY = 30,30
width, height = 12*sizeX, 12*sizeY
black = 0, 0, 0
screen = pygame.display.set_mode([width,height])
gridSize = int(width/grid), int(height/grid)
field = pygame.Rect(3, 3, 3, 3)

board = snake.board.Board(sizeX,sizeY)

colors = [[0,0,0],[0,100,200],[200,100,0],[100,200,0],[230,150,18],[255,0,0],[224,23,246],[23,231,246],[255,255,0],[160,160,0]]

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board.snake.rotateLeft()
            if event.key == pygame.K_RIGHT:
                board.snake.rotateRight()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    screen.fill(black)

    for segment in board.snake.segments:
        pygame.draw.rect(screen,colors[1],pygame.Rect(segment.x*grid,segment.y*grid,grid,grid))

    pygame.draw.rect(screen,colors[2],pygame.Rect(board.fruit.x()*grid,board.fruit.y()*grid,grid,grid))

    pygame.display.flip()

    rects = []
    board.update()
#    for x in board.next():
#        rect = pygame.Rect(x[0]*grid,x[1]*grid,grid,grid)
#        pygame.draw.rect(screen,colors[x[2]],rect)
#        rects.append(rect)
    #pygame.display.update(rects)
    clock.tick(20)
