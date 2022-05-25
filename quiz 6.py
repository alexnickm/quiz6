import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
YELLOW = (255, 255, 0)
ORANGE = (250, 100, 0)
BLACK = (0,0,0)
BACKGROUND = (255,255,255)
LIGHTP = (150, 0, 250)
PURPLE = (255,192,203)
pi = 3.14
pygame.draw.rect(screen, (BACKGROUND), (0,0,800,800))

class butterfly:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (LIGHTP), (self.xpos - 15, self.ypos+70), 40)
        pygame.draw.circle(screen, (LIGHTP), (self.xpos+50, self.ypos+70), 40)
        pygame.draw.circle(screen, (PURPLE), (self.xpos-15, self.ypos+40), 45)
        pygame.draw.circle(screen, (PURPLE), (self.xpos+50, self.ypos+40), 45)
        pygame.draw.ellipse(screen, (YELLOW), (self.xpos, self.ypos, 40, 130))
        pygame.draw.aaline(screen, (BLACK), (self.xpos - 15, self.ypos - 25), (self.xpos+15, self.ypos+20), 20)
        pygame.draw.aaline(screen, (BLACK), (self.xpos+40, self.ypos-25), (self.xpos+25, self.ypos+20), 20)
        pygame.draw.arc(screen, (ORANGE), (self.xpos+1,self.ypos+50, 40,50), 5*pi/4, 7*pi/4, 3)
        pygame.draw.arc(screen, (ORANGE), (self.xpos+1,self.ypos+35, 40,50), 5*pi/4, 7*pi/4, 3)
        pygame.draw.arc(screen, (ORANGE), (self.xpos+1,self.ypos+25, 40,50), 5*pi/4, 7*pi/4, 3)
        pygame.draw.arc(screen, (ORANGE), (self.xpos+1,self.ypos+15, 40,50), 5*pi/4, 7*pi/4, 3)
      

butterfly1 = butterfly (350,350)

butterfly1.draw()

pygame.display.flip()
