import tools
import sys
import pygame
from pygame.locals import *

sheet = tools.SpriteSheet('resources/spritesheet.png')
sprites = sheet.get_sheet((0, 0, 16, 16), 21, 5)

pygame.init()
main_clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((255, 255))
pygame.display.set_caption('ICS4U Tile Based Game')
display_surface.fill((0, 0, 0), (0, 0, 255, 255))

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
    display_surface.blit(sprites[2][10], (0, 0))
    display_surface.blit(sprites[2][11], (16, 0))
    display_surface.blit(sprites[3][10], (0, 16))
    display_surface.blit(sprites[3][11], (16, 16))
    main_clock.tick(60)
