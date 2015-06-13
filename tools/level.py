import pygame
import tools.screen

class Level(object):
    def __init__(self, level, resolution, tile_size, player):
        # initialize background
        sheet = tools.SpriteSheet('resources/background1.png')
        background_sprites = sheet.get_sheet((0, 0, 16, 16), 10, 10)

        background_map = tools.Screen(resolution, tile_size)
        background_map.background('resources/' + level + '/background.txt', background_sprites)
        self.background = background_map.screen

        # initialize boundaries
        self.bounds = tools.BoundMap('resources/' + level + '/boundaries.txt', tile_size)

        # initialize entities
        self.entities = tools.Entities('resources/' + level + '/entities.txt', player, tile_size)
