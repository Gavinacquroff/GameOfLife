"""Show intro screen and play button"""
from time import sleep
import os
import sys
import pygame

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def intro (screen):
    """function"""
    asset_url = resource_path('assets/play_hover.png')
    img_hovered = pygame.image.load(asset_url)

    asset_url = resource_path('assets/play.png')
    img = pygame.image.load(asset_url)

    asset_url = resource_path('assets/Game_of_Life.png')
    bgrnd = pygame.image.load(asset_url)

    # img_hovered = pygame.image.load("play_hover.png")
    # img = pygame.image.load("play.png")
    # bgrnd = pygame.image.load('Game_of_Life.png')

    rect = pygame.Rect(140, 392, 197, 75)

    screen.blit(bgrnd, (0, 0))
    screen.blit(img, rect)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pos = pygame.mouse.get_pos()
            if (rect.collidepoint(pos)):
                screen.blit(img_hovered, rect)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    sleep(1)
            else:
                screen.blit(img, rect)
                pygame.display.update()
    
    screen.fill((0, 0, 0)) # clear screen with black color

    pygame.display.flip()

