import pygame
from pygame.locals import *

class SpriteOff:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def is_off_screen(sprite):
        return sprite.rect[0] < -(sprite.rect[2])
