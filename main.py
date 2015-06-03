import tools
import sys
import pygame
from pygame.locals import *

# Constants
resolution = (511, 511)

# Initialize background
background = pygame.Surface(resolution)
sheet = tools.SpriteSheet('resources/background1.png')
background_sprites = sheet.get_sheet((0, 0, 16, 16), 21, 5)
background_map = tools.Screen('resources/level1.background', background_sprites)

for n, i in enumerate(background_map.textmap):
    for m, j in enumerate(i):
        background.blit(j, (32 * m, 32 * n))

# initialize PyGame
pygame.init()
main_clock = pygame.time.Clock()

display_surface = pygame.display.set_mode(resolution)
pygame.display.set_caption('ICS4U Tile Based Game')
display_surface.blit(background, (0, 0))  # draw background to screen

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            pass
            if event.key == K_UP:
                pass
            elif event.key == K_DOWN:
                pass
            elif event.key == K_LEFT:
                pass
            elif event.key == K_RIGHT:
                pass
        
        pygame.display.update()
    display_surface.blit(background, (0, 0))
    main_clock.tick(60)
