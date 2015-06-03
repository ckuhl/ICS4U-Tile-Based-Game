import pygame


class Screen(object):
    def __init__(self, mapfile, spritesheet, resolution):
        """
        Creates a background screen from given a given map file.
        :param mapfile: A map of the sprites in the level
        :param spritesheet: The list of lists of sprites to be used
        :param resolution: The resolution of the screen
        :return: A Surface object with the background drawn on.
        """
        with open(mapfile, 'r') as file:
            self.textmap = [[pygame.transform.scale2x(spritesheet[int(y, 16) // 21][int(y, 16) % 21]) for y in x.split()] for x in file]

        self.screen = pygame.Surface(resolution)

        for n, i in enumerate(self.textmap):
            for m, j in enumerate(i):
                self.screen.blit(j, (32 * m, 32 * n))
