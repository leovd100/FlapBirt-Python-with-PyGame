import pygame
from pygame.locals import *
from bird import Bird
from ground import Ground
from spriteOffScreen import SpriteOff
from commands import Commands

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 650
BACKGROUND = pygame.image.load('./sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
GROUND_WIDTH = 2 * SCREEN_WIDTH



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


bird_group = pygame.sprite.Group()
bird = Bird(SCREEN_WIDTH, SCREEN_HEIGHT)
bird_group.add(bird)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground( SCREEN_WIDTH,GROUND_WIDTH * i)
    ground_group.add(ground)



# Controla o FPS 
clock = pygame.time.Clock()

while True:
    # Seta o FPS, clock do jogo
    clock.tick(30)
    for event in pygame.event.get():
        Commands.keyCommands(bird, event)
    screen.blit(BACKGROUND, (0,0))


    if SpriteOff.is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])
        
        new_ground = Ground(SCREEN_WIDTH,GROUND_WIDTH -20)
        ground_group.add(new_ground)


    bird_group.update()
    ground_group.update()

    bird_group.draw(screen)
    ground_group.draw(screen)
    pygame.display.update()
