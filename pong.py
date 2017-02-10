import sys, pygame, pong.ball, pong.paddle, nNet.controller, analyser.analyser, renderer
pygame.init()

size = width, height = 1000,800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pong.ball.Ball(width,height)
paddle = pong.paddle.Paddle(20,height/2)

population = 40
controller = nNet.controller.Controller(population,3,1,1,4,0.7,0.05)
trained = 0
fitness = []
aiDummyIndex = 0

analyser = analyser.analyser.Analyser(height, width, population)
analyser.update([0 for i in xrange(population+1)], controller.geneticAlg.chromosomes)

def draw():
    white = (255,255,255)
    pygame.draw.rect(screen,white,(ball.rect))
    pygame.draw.rect(screen,white,(paddle.rect))

drawAll = renderer.createDrawAllFunction(draw, width, height)

def playerMovement():
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        paddle.move(1,height)
    if key[pygame.K_DOWN]:
        paddle.move(-1,height)
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
    return [normalXVector, normalYVector, ballYVelocity]

def parseOutput(output):
    return output[0]*2.0 -1.0

def movePaddleNeuralNet(paddle,index):
    _in = getInput(paddle)
    _out = controller.getOutput(_in,index)
    print "input :", _in, "output :", _out
    paddle.move(parseOutput(_out),height)

mode = "run"
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_a:
                if mode == "run":
                    mode = "analyse"
                else:
                    mode = "run"

    if mode == "run":
        movePaddleNeuralNet(paddle,trained)
        playerMovement()
        if ball.tick(width,height,paddle) == -1:
            fitness.append(paddle.score)
            trained += 1
            paddle.reset()
            if population <= trained:
                controller.evolve(fitness)
                analyser.update(fitness, controller.geneticAlg.chromosomes)
                fitness = []
                trained = 0
        drawAll(screen, trained, controller.generation, paddle.score)
    elif mode == "analyse":
        analyser.draw(screen)

    pygame.display.flip()
