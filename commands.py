import pygame
from pygame.locals import *
from bird import Bird

class Commands:
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)



    def keyCommands(bird, event):
        if event.type == QUIT:
            pygame.quit()
    

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()