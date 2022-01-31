import pygame
from sys import exit

pygame.init()


# create display surface
SCREEN = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Typing Trainer')

# clock object
clock = pygame.time.Clock()


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    SCREEN.fill('Black')

    # update (reload) the screen every clock tick
    pygame.display.update()

    # clock tick frequency = 60fps
    # refreshes about 60 times per second
    clock.tick(60)