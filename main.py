import tools
import sys
import pygame
from pygame.locals import *

sheet = tools.SpriteSheet('resources/spritesheet.png')
sprite = sheet.get_image((0, 0, 16, 16))

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
    display_surface.blit(sprite, (0, 0))
    main_clock.tick(60)