import pygame


class Entity(object):
    def __init__(self, position, tile_size, sprites=None, updates_per_frame=1):
        """
        Creates basic Entity object, containing x, y position, direction, and sprites (if necessary)
        :param position: integer tuple
        :param tile_size: integer tuple
        :param sprites: array of sprites
        :param updates_per_frame: integer indicating the number of position updates per sprite frame change
        :return: None
        """
        self.x = position[0] * tile_size[0]
        self.y = position[1] * tile_size[1]
        self.dir = 2
        self.height = 1

        if sprites:
            self.sprites = [[pygame.transform.scale2x(x) for x in y] for y in sprites]
            self.frames = len(self.sprites)
            self.current_frame = 0
            self.current_sprite = self.sprites[self.dir][self.current_frame]
            self.updates_per_frame = updates_per_frame
            self.update_counter = 0

    def update(self, direction=None):
        """
        Updates current sprite (in animation cycle) and direction of sprite
        :param direction: The direction of sprite: 0: N, 1: E, 2: S, 3: W
        :return: None
        """
        self.update_counter += 1

        if self.update_counter == self.updates_per_frame:
            self.update_counter = 0
            self.current_frame = (self.current_frame + 1) % (self.frames)
            self.current_sprite = self.sprites[self.dir][self.current_frame]

        if direction is not None:
            self.dir = direction

# TODO: Create subclasses of Entity for the different entities (character, enemy etc.)


class Entities(object):
    def __init__(self, entitylist, tile_size):
        # TODO: work in progress, should be analogous to BoundList when finished
        with open(entitylist, 'r') as file:
            entities = [x.strip().split() for x in file]
        print(entities)
