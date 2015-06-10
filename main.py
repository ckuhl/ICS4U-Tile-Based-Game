import tools
import sys
import pygame
from pygame.locals import *

# constants
resolution = (511, 511)
tile_size = (32, 32)

# initialize background
sheet = tools.SpriteSheet('resources/background1.png')
background_sprites = sheet.get_sheet((0, 0, 16, 16), 10, 10)

background_map = tools.Screen(resolution, tile_size)
background_map.background('resources/level1.background', background_sprites)

# initialize level boundaries
bounds = tools.BoundMap('resources/level1.boundaries', tile_size)

# initialize entities
entities = tools.Entities('resources/level1.entities')
player = entities.player

# initialize PyGame
pygame.init()
main_clock = pygame.time.Clock()
display_surface = pygame.display.set_mode(resolution)
pygame.display.set_caption('ICS4U Tile Based Game')
pygame.display.set_icon(pygame.image.load('resources/icon.png'))

display_surface.blit(background_map.screen, (0, 0))  # draw background to screen

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # handle keyboard input
    diagonal_check = False
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        if bounds.rect_membership((player.x, player.y - 1), tile_size, player):
            player.y -= 1
        diagonal_check = True
        player.update(0)

    elif keys[K_DOWN]:
        if bounds.rect_membership((player.x, player.y + 1), tile_size, player):
            player.y += 1
        diagonal_check = True
        player.update(2)

    if keys[K_LEFT]:
        if bounds.rect_membership((player.x - 1, player.y), tile_size, player):
            player.x -= 1
        if not diagonal_check:
            player.update(3)

    elif keys[K_RIGHT]:
        if bounds.rect_membership((player.x + 1, player.y), tile_size, player):
            player.x += 1
        if not diagonal_check:
            player.update(1)

    # back-to-front blitting of images
    display_surface.blit(background_map.screen, (0, 0))
    display_surface.blit(player.current_sprite, (player.x, player.y - 8))  # y shifted down 8 px to look proper

    # TODO: Handle multiple levels, and transitions between levels (activated by Doors)

    pygame.display.update()
    main_clock.tick(60)
