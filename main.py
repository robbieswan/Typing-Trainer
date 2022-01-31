import pygame
from sys import exit

pygame.init()


# create display surface
<<<<<<< HEAD
SCREEN = pygame.display.set_mode((800, 400))
=======
screen = pygame.display.set_mode((800, 400))
>>>>>>> 61d72448f3621241c39655e34ec607cb1d4a5b01
pygame.display.set_caption('Typing Trainer')

# clock object
clock = pygame.time.Clock()


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

<<<<<<< HEAD
    SCREEN.fill('Black')
=======
    screen.fill('Black')
>>>>>>> 61d72448f3621241c39655e34ec607cb1d4a5b01

    # update (reload) the screen every clock tick
    pygame.display.update()

    # clock tick frequency = 60fps
    # refreshes about 60 times per second
<<<<<<< HEAD
    clock.tick(60)
=======
    clock.tick(60)
>>>>>>> 61d72448f3621241c39655e34ec607cb1d4a5b01
