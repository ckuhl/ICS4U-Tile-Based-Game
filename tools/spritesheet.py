import pygame


class SpriteSheet(object):
    def __init__(self, sheetname):
        """
        Loads the sheet into memory.
        :param sheetname: string -- location of sheet
        :return: None
        """
        try:
            self.sheet = pygame.image.load(sheetname)
        except pygame.error:
            print('Unsupported image format!')

    def delta(self, coords):
        """
        Gives the change in x and y of a given pair of coordinates.
        :param coords: integer 4-tuple
        :return: integer tuple
        """
        return coords[2] - coords[0], coords[3] - coords[1]

    def get_image(self, coords):
        """
        Grabs a single image from a spritesheet, given its coordinates.
        :param coords: integer 4-tuple -- the sprites coordinates (x1, y1, x2, y2)
        :return: pygame.Surface
        """
        sprite = pygame.Surface(self.delta(coords), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), coords)
        return sprite

    def get_line(self, coords, nx):
        """
        Calls get_image for a row of sprites
        :param coords: integer 4-tuple -- leftmost sprite's coordinates (x1, y1, x2, y2)
        :param nx: integer -- number of sprites in each row
        :return: list of pygame.Surface
        """
        dx = self.delta(coords)[0]
        return [self.get_image((coords[0] + dx * x, coords[1], coords[2] + dx * x, coords[3])) for x in range(nx)]

    def get_sheet(self, coords, nx, ny):
        """
        Calls get_line for a sheet of sprites.
        :param coords: integer 4-tuple -- top left sprite's coordinates (x1, y1, x2, y2)
        :param nx: integer -- number of sprites in each row
        :param ny: integer -- number of sprites in each column
        :return: list of a list of pygame.Surface
        """
        dx, dy = self.delta(coords)
        return [self.get_line((coords[0], coords[1] + dy * x, coords[2], coords[3] + dy * x), nx) for x in range(ny)]
