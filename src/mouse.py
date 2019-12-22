"""mouse.py
Enables mouse click selection of initial states
"""
import pygame
from pygame import QUIT, K_ESCAPE, MOUSEBUTTONDOWN, KEYDOWN

STEPS = 20
SIZE_S = 49
SIZE_L = 500

def set_state(screen, small_screen):
    """user selection of GoL initial state"""
    setup = True
    while setup:
        for event in pygame.event.get():
            small_arr = pygame.PixelArray(small_screen)
            if event.type == QUIT:
                setup = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                setup = False
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #print ('Mouse at ' + str(pos))
                small_pos = ((int)(pos[0]/(SIZE_L/SIZE_S)), (int)(pos[1]/(SIZE_L/SIZE_S)))
                #print ('Setting small arr pos ' + str(small_pos))
                small_arr[small_pos] = 0xFFFFFF
                small_arr.close()
                pygame.transform.scale(small_screen, (SIZE_L,SIZE_L), screen)
                pygame.display.flip()
