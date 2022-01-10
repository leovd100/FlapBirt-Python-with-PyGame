import pygame
from pygame.locals import *


GROUND_HEIGHT = 100
GAME_SPEED = 10

class Ground(pygame.sprite.Sprite):

    def __init__(self, width, xpos):
        GROUND_WIDTH = 2 * width
        SCREEN_HEIGHT = 650
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load('./sprites/base.png')
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH,GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT


    
    def update(self):
        self.rect[0] -= GAME_SPEED