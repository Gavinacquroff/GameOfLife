""" main.py"""

from time import sleep
# from pygame import QUIT, K_ESCAPE, MOUSEBUTTONDOWN, KEYDOWN
import pygame
import cells
import mouse
from intro import intro


STEPS = 20
SIZE_S = 49
SIZE_L = 500
SIZE_TEST = 3
TESTING = False

# initialize all pygame modules
pygame.init()

# create display surface
screen = pygame.display.set_mode((SIZE_L, SIZE_L))
# test_arr = pygame.PixelArray(screen)
# test_arr[:][0] = 0xFFFFFF
# test_arr.close()
# pygame.display.flip()
# input('test')

intro(screen)

# create small working surface
small_screen = pygame.Surface((SIZE_S,SIZE_S))

# set inital state
#cells.populate_surface(screen, small_screen)
mouse.set_state(screen, small_screen)

# play the game
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    sleep(0.1)
    small_arr = pygame.PixelArray(small_screen)

    # run rules on all cells
    cells.update_cells(small_arr)
    # close access to PixelArray
    small_arr.close()

    # scale and update screen
    pygame.transform.scale(small_screen, (SIZE_L,SIZE_L),screen)
    pygame.display.flip()
