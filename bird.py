import pygame
from pygame.locals import *

SPEED = 10
GRAVITY = 1

class Bird(pygame.sprite.Sprite):

    def __init__(self,w,h):
      
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('./sprites/bluebird-upflap.png').convert_alpha(),
                      pygame.image.load('./sprites/bluebird-midflap.png').convert_alpha(),
                      pygame.image.load('./sprites/bluebird-downflap.png').convert_alpha()]

        self.speed = SPEED 

        self.current_image = 0

        self.image = pygame.image.load('./sprites/bluebird-upflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect[0] = w/2
        self.rect[1] = h/2
       
    
    def update(self):
        
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += GRAVITY
        # Update height
        self.rect[1] += self.speed + GRAVITY


    def bump(self):  
        self.speed = -SPEED
