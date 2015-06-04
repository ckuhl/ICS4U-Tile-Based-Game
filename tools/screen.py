import pygame


class Screen(object):
    def __init__(self, resolution, tile_size):
        """
        Creates Surface the size of the screen, initializes some variables
        :param resolution: Integer tuple
        :param tile_size: Integer tuple
        :return: None
        """
        self.screen = pygame.Surface(resolution)
        self.tx = tile_size[0]
        self.ty = tile_size[1]

    def background(self, mapfile, spritesheet):
        """
        Draws background to previously initialized Surface object
        :param mapfile: 2D integer array in a text file
        :param spritesheet: 2D Surface array of sprites
        :return: None
        """
        width = len(spritesheet[0])

        # populate 2D array with sprites
        with open(mapfile, 'r') as file:
            self.textarray = [[pygame.transform.scale2x(spritesheet[int(y) // width][int(y) % width]) for y in x.split()] for x in file]

        # draw sprites to Surface
        for n, i in enumerate(self.textarray):
            for m, j in enumerate(i):
                self.screen.blit(j, (self.tx * m, self.ty * n))
