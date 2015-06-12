"""
Project expectations:
A1.3 demonstrate the ability to use non-numeric comparisons (e.g., strings, comparable interface) in computer programs;
A1.5 describe and use one-dimensional arrays of compound data types (e.g., objects, structures, records) in a computer
     program.
A2.2 use modular design concepts that support reusable code (e.g., encapsulation, inheritance, method overloading,
     method overriding, polymorphism);
A3.1 demonstrate the ability to read from, and write to, an external file (e.g., text file, binary file, database, XML
     file) from within a computer program;
A3.3 create subprograms to insert and delete array elements;
A4.1 work independently, using support documentation (e.g., IDE Help, tutorials, websites, user manuals), to resolve
     syntax issues during software development;
A4.3 create fully documented program code according to industry standards (e.g., doc comments, docstrings, block
     comments, line comments);
A4.4 create clear and maintainable external user documentation (e.g., Help files, training materials, user manuals).

B1.7 demonstrate the ability to use shared resources to manage source code effectively and securely (e.g., organize
     software components using shared files and folders with timestamps, and proper version control).
B2.2 demonstrate the ability to meet project goals and deadlines by managing individual time during a group project;

C1.1 decompose a problem into modules, classes, or abstract data types (e.g., stack, queue, dictionary) using an
     object-oriented design methodology (e.g., CRC [Class Responsibility Collaborator] or UML [Unified Modeling Language]);
C1.4 apply the principle of reusability in program design (e.g., in modules, subprograms, classes, methods, and
     inheritance).
"""
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
