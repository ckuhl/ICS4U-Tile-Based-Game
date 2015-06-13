import tools.screen


class Level(object):
    def __init__(self, level, resolution, tile_size, player):
        """
        A master class to hold all of the components of a level.
        :param level: string -- the name of the level
        :param resolution: integer tuple -- size of screen (width, height)
        :param tile_size: integer tuple -- size of a tile (width, height)
        :param player: tools.Player
        :return: None
        """
        # initialize background
        self.resolution = resolution
        self.fader = 0
        sheet = tools.SpriteSheet('resources/background1.png')
        background_sprites = sheet.get_sheet((0, 0, 16, 16), 10, 10)

        background_map = tools.Screen(resolution, tile_size)
        background_map.background('resources/' + level + '/background.txt', background_sprites)
        self.background = background_map.screen

        # initialize boundaries
        self.bounds = tools.BoundMap('resources/' + level + '/boundaries.txt', tile_size)

        # initialize entities
        self.entities = tools.Entities('resources/' + level + '/entities.txt', player, tile_size)
