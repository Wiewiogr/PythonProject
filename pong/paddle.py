import pygame

class Paddle(object):
    def __init__(self,left,top,width = 16,height = 120):
        self.height = height
        self.initRect = pygame.rect.Rect(left,top-height/2,width,height)
        self.rect = pygame.rect.Rect(self.initRect)
        self.score = 0

    #>0 up <0 down ==0 stay
    def move(self,where,height):
        if where > 0:
            if self.rect.y < 0:
                self.rect.y = 0
            else:
                self.rect.y -= (6*where)
        else:
            if self.rect.y > height - self.height:
                self.rect.y = height - self.height
            else:
                self.rect.y -= (6*where)

    def reset(self):
        self.rect = pygame.rect.Rect(self.initRect)
        self.score = 0
