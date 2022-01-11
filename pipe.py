import pygame, random
from pygame.locals import *

PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 100
GAME_SPEED = 10
class Pipe(pygame.sprite.Sprite):
    


    def __init__(self, inverted, xPos,ySize, SCREEN_HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./sprites/pipe-red.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xPos

        if inverted:
            self.image = pygame.transform.flip(self.image,False, True)
            self.rect[1] = -(self.rect[3] - ySize + PIPE_GAP)
        else:
            self.rect[1] = SCREEN_HEIGHT - ySize
  
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= GAME_SPEED

    def setGameSpeed(self,value):
        GAME_SPEED = value