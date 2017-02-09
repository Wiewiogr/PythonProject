import pygame
import random

class Ball(object):
    def __init__(self,sizeX,sizeY,radius = 8):
        self.initRect = pygame.rect.Rect(sizeX/2-radius,sizeY/2 - radius,radius*2,radius*2)
        self.rect = pygame.rect.Rect(self.initRect)
        self.initVelocity = 3
        self.xVelocity = self.initVelocity
        self.radius = radius
        self.yVelocity = self.initVelocity

    def reset(self):
        self.rect = pygame.rect.Rect(self.initRect)
        self.rect.x += random.randint(-50,50)
        self.rect.y += random.randint(-50,50)
        self.xVelocity = -self.initVelocity
        #self.xVelocity *= random.choice([-1,1])
        self.yVelocity *= random.choice([-1,1])

    #def tick(self,width,height,paddleLeft,paddleRight):
    def tick(self,width,height,paddleLeft):
        self.rect.x += self.xVelocity
        self.rect.y += self.yVelocity


        if self.rect.x < 0:
            self.xVelocity *= -1
            if paddleLeft.score < 1:
                paddleLeft.score = abs(paddleLeft.rect.y - self.rect.y)*1.0/(height*2)
                if paddleLeft.score < 0.1:
                    paddleLeft.score = 0.1
            #paddleRight.score += abs(1 - paddleLeft.score*5)/9.0
            self.reset()
            return -1
        if self.rect.x > width-2*self.radius:
            self.xVelocity *= -1
#            paddleRight.score += abs(paddleRight.rect.y - self.rect.y)*1.0/(height*5)
#            paddleLeft.score += abs(1 - paddleRight.score*5)/9.0
#            self.reset()
#            return -1
        if self.rect.y < 0:
            self.yVelocity *= -1
        if self.rect.y > height-2*self.radius:
            self.yVelocity *= -1

        if self.rect.colliderect(paddleLeft):
            self.xVelocity *= -1
            self.rect.left = paddleLeft.rect.right
            paddleLeft.score += 1
#        elif self.rect.colliderect(paddleRight):
#            self.xVelocity *= -1
#            self.rect.right = paddleRight.rect.left
#            paddleRight.score += 1


