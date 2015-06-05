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
            self.height_dict = {}

            # create rectangle from coordinates
            for line in file:
                line = line.strip().split()
                level, type, coords = int(line[0][0]), line[0][1:], [int(x) for x in line[1:]]
                rect = self.create_bounds(type, coords, tile_size)

                # add to height_dict
                try:
                    self.height_dict[level].append((rect, type))
                except KeyError:
                    self.height_dict[level] = [(rect, type)]

    def create_bounds(self, bound_type, coords, tile_size):
        """
        Creates a boundary rectangle given two points, and a type of boundary
        :param bound_type: String, type of boundary
        :param coords: Integer 4-tuple
        :param tile_size: Integer tuple
        :return: pygame.Rect
        """
        tx, ty = tile_size[0], tile_size[1]
        if bound_type[0] == 'D':
            return pygame.Rect(coords[0] * tx, coords[1] * ty, tx, ty)

        else:
            return pygame.Rect(coords[0] * tx, coords[1] * ty, tx * (coords[2] - coords[0] + 1), ty * (coords[3] - coords[1] + 1))

    def point_membership(self, point, height):
        """
        Checks if a point exists within a certain bounds
        :param point: Integer tuple
        :param height: List of pygame.Rect to check against
        :return: Boolean
        """
        for i in self.height_dict[height]:
            if i[0].collidepoint(point):
                return True
        return False

    def rect_membership(self, sprite_pos, tile_size, height):
        """
        Checks if a rectangle exists within
        :param sprite_pos: Top left corner of the sprite
        :param tile_size: Width and height of the sprite
        :param height: Height that the given entity exists at (1 - 9)
        :return: Boolean
        """

        sx, sy, tx, ty = sprite_pos[0], sprite_pos[1], tile_size[0], tile_size[1]
        points = [sprite_pos, (sx + tx - 1, sy), (sx, sy + ty - 1), (sx + tx - 1, sy + ty - 1)]

        for i in points:
            if not self.point_membership(i, height):
                return False
        return True

    # TODO: Implement a method between levels (ie stairs)
