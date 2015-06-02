import pygame


class SpriteSheet(object):
    def __init__(self, sheetname):
        try:
            self.sheet = pygame.image.load(sheetname)
        except pygame.error:
            print('Unsupported image format!')

    def delta(self, coords):
        """
        Gives the change in x and y of a given pair of coordinates.
        :param coords: Integer 4-tuple
        :return: Integer tuple
        """
        return coords[2] - coords[0], coords[3] - coords[1]

    def get_image(self, coords):
        """
        Grabs a single image from a spritesheet, given its coordinates.
        :param coords: (x1, y1, x2, y2) tuple of the sprites coordinates
        :return: Pygame surface object
        """
        sprite = pygame.Surface(self.delta(coords))
        sprite.blit(self.sheet, (0, 0), coords)
        return sprite

    def get_line(self, coords, nsprites):
        """
        Calls get_image for a row of sprites
        :param coords: Integer 4-tuple: The coordinates of the first sprite
        :param nsprites: Integer: The number of sprites in the row.
        :return: A list of PyGame surface objects
        """
        dx = self.delta(coords)[0]
        return [self.get_image((coords[0] + dx * x, coords[1], coords[2] + dx * x, coords[3])) for x in range(nsprites)]

    def get_sheet(self, coords, nx, ny):
        """
        Calls get_line for a sheet of sprites.
        :param coords: Integer 4-tuple: The coordinates of the top left sprite.
        :param nx: Integer: The number of sprites in the x direction.
        :param ny: Integer: The number of sprites in the y direction.
        :return: A list of list of Pyame surface objects.
        """
        dx, dy = self.delta(coords)
        return [self.get_line((coords[0], coords[1] + dy * x, coords[2], coords[3] + dy * x), nx) for x in range(ny)]
