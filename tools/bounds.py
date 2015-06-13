import pygame


class BoundMap(object):
    def __init__(self, bound_map, tile_size):
        """
        Creates a list of (type, boundary) tuples given an input boundary map and the size of each tile
        :param bound_map: string -- the name of the file to open
        :param tile_size: 1 char string
        :return: None
        """
        # convert coordinates to integers
        with open(bound_map, 'r') as file:
            self.height_dict = {}

            # create rectangle from coordinates
            for line in file:
                line = line.strip().split()
                level, bound_type, coords = int(line[0][0]), line[0][1:], [int(x) for x in line[1:]]
                rect = self.create_bounds(coords, tile_size)

                # add bounds to proper levels
                if bound_type == 'A':
                    self.add_to_dict(rect, bound_type, level + 1)
                elif bound_type == 'B':
                    self.add_to_dict(rect, bound_type, level - 1)

                else:
                    self.add_to_dict(rect, bound_type, level)

    def create_bounds(self, coords, tile_size):
        """
        Creates a boundary rectangle given two points and size
        :param coords: integer 4-tuple
        :param tile_size: integer tuple
        :return: pygame.Rect
        """
        tx, ty = tile_size[0], tile_size[1]
        return pygame.Rect(coords[0] * tx, coords[1] * ty, tx * (coords[2] - coords[0] + 1), ty * (coords[3] - coords[1] + 1))

    def point_membership(self, point, height):
        """
        Checks if a point exists within a certain bounds
        :param point: integer tuple
        :param height: integer -- the height of the level to check against
        :return: Boolean
        """
        for i in self.height_dict[height]:
            if i[0].collidepoint(point):
                return i[1]
        return False

    def rect_membership(self, sprite_pos, tile_size, entity):
        """
        Checks if a rectangle exists within
        :param sprite_pos: integer tuple -- the top left corner of the sprite
        :param tile_size: integer tuple -- (width, height) of the sprite
        :param entity: tools.Entity (or subclass) -- The entity to check the position of
        :return: Boolean
        """
        height = entity.height
        sx, sy, tx, ty = sprite_pos[0], sprite_pos[1], tile_size[0], tile_size[1]
        points = [sprite_pos, (sx + tx - 1, sy), (sx, sy + ty - 1), (sx + tx - 1, sy + ty - 1)]

        # set comprehension of  where the corners land
        corner_types = [self.point_membership(x, height) for x in points]
        # if the front is ascending stairs, check if rear is up the level
        if corner_types[2:] == ['B', 'B']:
            if False not in [self.point_membership(x, height) for x in points[:2]]:
                entity.height += 1

        # if the front is down the stairs, check if the rear is down the level
        elif corner_types[:2] == ['A', 'A']:
            if False not in [self.point_membership(x, height) for x in points[2:]]:
                entity.height -= 1

        # if any corner is out of bounds
        if False in corner_types:
            return False

        return entity.height

    def add_to_dict(self, rect, bound_type, height):
        """
        Appends (Rect, type) tuple to list of bounds in bounds_dict[height]
        :param rect: pygame.Rect -- the rectangle defining bounds
        :param bound_type: 1 char string -- the ID of the Entity type (door, stairs, etc)
        :param height: integer -- the current height
        :return: None
        """
        try:
            self.height_dict[height].append((rect, bound_type))
        except KeyError:
            self.height_dict[height] = [(rect, bound_type)]
