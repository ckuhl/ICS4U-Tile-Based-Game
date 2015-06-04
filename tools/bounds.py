import pygame


class BoundMap(object):
    def __init__(self, boundmap, tile_size):
        """
        Creates a list of (type, boundary) tuples given an input boundary map and the size of each tile
        :param boundmap: File containing a type and two points per line
        :param tile_size: String, one char
        :param resolution: Integer tuple
        :return: None
        """
        # convert coordinates to integers
        with open(boundmap, 'r') as file:
            self.bounds = []

            for line in file:
                # create rectangle from coordinates
                rect = self.create_bounds([line[0]], [int(x) for x in line.strip().split()[1:]], tile_size)
                self.bounds.append((line[0], rect))

    def create_bounds(self, bound_type, coords, tile_size):
        """
        Creates a boundary rectangle given two points, and a type of boundary
        :param bound_type: String, type of boundary
        :param coords: Integer 4-tuple
        :param tile_size: Integer tuple
        :return: pygame.Rect
        """
        tx, ty = tile_size[0], tile_size[1]

        # half height for door (due to entering it)
        if bound_type == 'D':
            return pygame.Rect(coords[0] * tx, coords[1] * ty + ty // 2, (coords[2] + 1) * tx - 1, (coords[3] + 1) * ty - 1)

        else:
            return pygame.Rect(coords[0] * tx, coords[1] * ty, (coords[2] + 1) * tx - 1, (coords[3] + 1) * ty - 1)

    def membership(self, sprite_rect):
        """
        Checks if a given sprite exists within the given boundaries.
        :param sprite_rect: pygame.Rect
        :return: Boolean
        """
        for i in self.bounds:
            if i[1].contains(sprite_rect):
                return True
        return False