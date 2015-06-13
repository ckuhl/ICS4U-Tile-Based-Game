import pygame


class Screen(object):
    def __init__(self, resolution, tile_size):
        """
        Creates Surface the size of the screen, initializes some variables
        :param resolution: integer tuple -- size of screen (width, height)
        :param tile_size: integer tuple -- size of a tile (width, height)
        :return: None
        """
        self.screen = pygame.Surface(resolution)
        self.tx = tile_size[0]
        self.ty = tile_size[1]
        self.text_array = None

    def background(self, mapfile, spritesheet):
        """
        Draws background to previously initialized Surface object
        :param mapfile: string -- location of the sheet
        :param spritesheet: list of lists of pygame.Surface
        :return: None
        """
        width = len(spritesheet[0])

        # populate 2D array with sprites
        with open(mapfile, 'r') as file:
            self.text_array = [[pygame.transform.scale2x(spritesheet[int(y) // width][int(y) % width]) for y in x.split()] for x in file]

        # draw sprites to Surface
        for n, i in enumerate(self.text_array):
            for m, j in enumerate(i):
                self.screen.blit(j, (self.tx * m, self.ty * n))
