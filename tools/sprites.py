import pygame


class SpriteSheet(object):
    def __init__(self, sheetname):
        try:
            self.sheet = pygame.image.load(sheetname)
        except pygame.error:
            print('Unsupported image format!')

    def get_image(self, coords):
        """
        Grabs a single image from a spritesheet, given its coordinates.
        :param coords: (x1, y1, x2, y2) tuple of the sprites coordinates
        :return: Pygame surface object
        """
        dx, dy = coords[2] - coords[0], coords[3] - coords[1]
        sprite = pygame.Surface((dx, dy))
        sprite.blit(self.sheet, (0, 0), coords)
        return sprite

    def get_line(self, coords, size):  # TODO: call get_image repeatedly
        pass

    def get_sheet(self, coords, size):  # TODO: call get_line repeatedly
        pass