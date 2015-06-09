import pygame
import tools.spritesheet


class Entities(object):
    def __init__(self, entity_file):
        """
        Populates a list of entities from the entities file
        :param entity_file: The name of the entity file to read from.
        :return: Entities object
        """
        self.entity_list = []
        self.player = None

        with open(entity_file, 'r') as file:
            for line in file:
                arguments = line.strip().split()
                entity_id, pos = arguments[0], (int(arguments[1]), int(arguments[2]))
                self.entity_list.append(self.create_entity(entity_id, pos))

    def create_entity(self, entity_id, pos):
        """
        A glorified switch statement, it creates entities according to their ID
        :param entity_id: 1 char string -- determines which kind of entity to create
        :param pos: (x, y) integer tuple -- position of the top left corner of the entity
        :return: Entity subclass
        """
        if entity_id == 'P':
            self.player = Player(pos)
        else:
            return "Entity type does not exist"


class Entity(object):
    """
    The parent class for entities, it initializes the entities position, level (height), and direction.
    Animations/sprites are also initialized if they exist.

    Entity.update(dir) updates the sprite's position, direction, and current frame (if animated)
    """
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


class Player(Entity):
    """
    The Player class contains additional variables and sprites.
    """
    def __init__(self, position):
        """
        Initializes the entity, from position
        :param position: (x, y) integer tuple -- top left of the sprite
        :return: None
        """
        player_sheet = tools.SpriteSheet('resources/player.png').get_sheet((0, 0, 16, 16), 8, 3)
        sprite_list = [player_sheet[0][:4], player_sheet[1][4:], player_sheet[0][4:], player_sheet[1][:4]]

        Entity.__init__(self, position, tile_size=(32, 32), sprites=sprite_list, updates_per_frame=6)

# TODO: Create entity subclass for doors
