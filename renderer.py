import sys, pygame, pong.ball, pong.paddle, nNet.controller, analyser
pygame.init()

size = width, height = 1200,800
black = (0, 0, 0)
white = (255,255,255)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pong.ball.Ball(width,height)
paddleLeft = pong.paddle.Paddle(20,height/2)
paddleRight = pong.paddle.Paddle(width - 30,height/2)

population = 40
controller = nNet.controller.Controller(population,5,1,1,5,0.7,0.05)
font = pygame.font.Font(None,30)
trained = 0
fitness = []
aiDummyIndex = 0

analyser = analyser.Analyser(height, width, population)
analyser.update()

def drawAll():
    screen.fill(black)
    pygame.draw.rect(screen,white,(ball.rect))
    pygame.draw.rect(screen,white,(paddleLeft.rect))
    pygame.draw.rect(screen,white,(paddleRight.rect))
    screen.blit(font.render("num "+str(trained)+" left score : "+str(paddleLeft.score),1,(255,255,255)),[10,10])
    screen.blit(font.render("num "+str(trained+1)+" right score : "+str(paddleRight.score),1,(255,255,255)),[900,10])
    screen.blit(font.render("generation : "+str(controller.generation),1,(255,255,255)),[550,10])

def playerMovement():
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        paddleLeft.move(1,height)
    if key[pygame.K_DOWN]:
        paddleLeft.move(-1,height)
    if key[pygame.K_w]:
        paddleRight.move(1,height)
    if key[pygame.K_s]:
        paddleRight.move(-1,height)

def getInput(paddle):
    normalHeight = paddle.rect.y*2.0/height-1.0
    normalXVector = abs(ball.rect.x-paddle.rect.x)*2.0/width-1
    normalYVector = (ball.rect.y - paddle.rect.y)*1.0/height
    ballYVelocity = ball.yVelocity/3.0
    side = 1
    if paddle.rect.x > width/2.0:
        side *= -1
    ballXVelocity = ball.xVelocity/3.0 * side
    #return [abs(ball.rect.y - paddle.rect.y)*1.0/height,ball.rect.y*1.0/height]
    return [normalHeight, normalXVector, normalYVector, ballYVelocity, ballXVelocity ]
#    return [ball.xVelocity/9.0,ball.yVelocity/9.0,
#            1.0*ball.rect.x/width,1.0*ball.rect.y/height,
#            1.0*paddle.rect.y/height]

def parseOutput(output):
    return output[0]*2.0 -1.0
  #  if output[0] > 0.5:
  #      return 1
  #  else:
  #      return -1
   # choice = output.index(max(output))
   # if choice == 0:
   #     return 1
   # elif choice == 1:
   #     return -1
   # elif choice == 2:
   #     return 0

def movePaddleNeuralNet(paddle,index):
    _in = getInput(paddle)
    print "input : ", _in
    output = controller.getOutput(_in,index)
    print index," : ",output
    paddle.move(parseOutput(output),height)

mode = "run"
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                if mode == "run":
                    mode = "analyse"
                else:
                    mode = "run"

    if mode == "run":
        movePaddleNeuralNet(paddleLeft,trained)
        movePaddleNeuralNet(paddleRight,aiDummyIndex)
        playerMovement()
        if ball.tick(width,height,paddleLeft,paddleRight) == -1:
            fitness.append(paddleLeft.score)
            #fitness.append(paddleRight.score)
            trained += 1
            paddleLeft.reset()
            paddleRight.reset()
            if population <= trained:
                print "fitnesses:"
                print fitness
                aiDummyIndex = fitness.index(max(fitness))
                controller.evolve(fitness)
                fitness = []
                trained = 0
        drawAll()
    elif mode == "analyse":
        analyser.draw(screen)

    pygame.display.flip()
    #clock.tick(120)
