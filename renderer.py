import pygame
pygame.init()
font = pygame.font.Font(None,30)
black = (0, 0, 0)
white = (255, 255, 255)

def createDrawAllFunction(fun, width, height):
    def drawAll(screen, trained, generation, score):
        screen.fill(black)
        screen.blit(font.render("num "+str(trained)+" score : "+str(score),1,white),[10,10])
        screen.blit(font.render("generation : "+str(generation),1,white),[(width/2)-50,10])
        fun()
    return drawAll



