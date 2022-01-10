import pygame
from pygame.locals import *


GAME_OVER_WIDTH = 200
GAME_OVER_HEIGHT = 80

class GameOver(pygame.sprite.Sprite):

    def __init__(self, w ,h):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./sprites/gameover.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GAME_OVER_WIDTH, GAME_OVER_HEIGHT))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[0] = w/2 - (GAME_OVER_WIDTH / 2)
        self.rect[1] = h/4 

    def update(self):
        pass





