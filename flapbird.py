import pygame, random
from pygame.locals import *
from bird import Bird
from ground import Ground
from spriteOffScreen import SpriteOff
from commands import Commands
from gameOver import GameOver
from pipe import Pipe
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 650

def backGroundRandom():
    value = random.randint(1,2)
    if value == 1:
        return './sprites/background-day.png'
    else: 
        return './sprites/background-night.png'

BACKGROUND = pygame.image.load(backGroundRandom())
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))



GROUND_WIDTH = 2 * SCREEN_WIDTH
GAME_SPEED = 10




def get_random_pipes(xPos):
    size = random.randint(100,300)
    pipe = Pipe(False, xPos, size,SCREEN_HEIGHT)
    pipe_inverted = Pipe(True, xPos, SCREEN_HEIGHT - size, SCREEN_HEIGHT)
    pipe.setGameSpeed(random.randint(130,200))
    pipe_inverted.setGameSpeed(random.randint(130,200))
    return (pipe, pipe_inverted)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


bird_group = pygame.sprite.Group()
bird = Bird(SCREEN_WIDTH, SCREEN_HEIGHT)
bird_group.add(bird)


game_over_group = pygame.sprite.Group()
game_over = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT)
game_over_group.add(game_over)


ground_group = pygame.sprite.Group()

for i in range(2):
    ground = Ground( SCREEN_WIDTH,GROUND_WIDTH * i)
    ground_group.add(ground)


pipe_group = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(SCREEN_WIDTH * i + 500)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])



# Controla o FPS 
clock = pygame.time.Clock()
gameOver = False
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

    if SpriteOff.is_off_screen(pipe_group.sprites()[0]) and gameOver == False:
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.remove(pipe_group.sprites()[0])

        pipes = get_random_pipes(SCREEN_WIDTH * 2)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])


    bird_group.update()
    ground_group.update()
    pipe_group.update()
    
    if (pygame.sprite.groupcollide(bird_group, ground_group,False,False, pygame.sprite.collide_mask) or 
       pygame.sprite.groupcollide(bird_group, pipe_group,False,False, pygame.sprite.collide_mask)) :
        # Game Over
        gameOver = True        
        print(gameOver)
    if gameOver == True:
        game_over_group.draw(screen)
        bird_group.remove(bird)
        pipe_group.remove(pipes[0])
        pipe_group.remove(pipes[1])
        
        #break


    bird_group.draw(screen)
    pipe_group.draw(screen)
    ground_group.draw(screen)
    
    
    pygame.display.update()
