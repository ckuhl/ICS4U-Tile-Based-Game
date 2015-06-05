import pygame


class BoundMap(object):
    def __init__(self, boundmap, tile_size):
        """
        Creates a list of (type, boundary) tuples given an input boundary map and the size of each tile
        :param boundmap: File containing a type and two points per line
        :param tile_size: String, one char
        :return: None
        """
        # convert coordinates to integers
        with open(boundmap, 'r') as file:
            self.bounds = []

            # create rectangle from coordinates
            for line in file:
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
        if bound_type == 'D':
            return pygame.Rect(coords[0] * tx, coords[1] * ty, tx, ty)

        else:
            return pygame.Rect(coords[0] * tx, coords[1] * ty, tx * (coords[2] - coords[0] + 1), ty * (coords[3] - coords[1] + 1))

    def membership(self, sprite_pos, tile_size):
        """
        Checks if a given sprite exists within the given boundaries.
        :param sprite_pos: integer tuple: top left corner of sprite
        :param tile_size: integer tuple: width and height of sprite
        :return: Boolean
        """
        for i in self.bounds:
            if i[1].contains(sprite_pos, tile_size):
                return True
        return False
