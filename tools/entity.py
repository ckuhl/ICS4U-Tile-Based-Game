import pygame
import tools.spritesheet


class Entities(object):
    def __init__(self, entity_file, player, tile_size):
        """
        Populates a list of entities from the entities file
        :param entity_file: The name of the entity file to read from.
        :return: Entities object
        """
        self.entity_list = []
        self.player = player

        with open(entity_file, 'r') as file:
            for line in file:
                arguments = line.strip().split()
                entity_id, pos = arguments[0], (int(arguments[1]), int(arguments[2]))
                try:
                    flag = arguments[3]
                except IndexError:
                    flag = None

                entity = self.create_entity(entity_id, pos, tile_size, flag)
                if entity:
                    self.entity_list.append(entity)

    def create_entity(self, entity_id, pos, tile_size, flag):
        """
        A glorified switch statement, it creates entities according to their ID
        :param entity_id: 1 char string -- determines which kind of entity to create
        :param pos: (x, y) integer tuple -- position of the top left corner of the entity
        :param flag: string or None -- identifies what level to jump to
        :return: Entity subclass
        """
        if entity_id == 'P':
            self.player.x, self.player.y = pos[0] * tile_size[0], pos[1] * tile_size[1]
            return False
        elif entity_id == 'D':
            return Door(pos, flag)
        else:
            raise KeyError

    def collisions(self):
        return [self.entity_list[y] for y in self.player.rect.collidelistall([x.rect for x in self.entity_list])]


class Entity(object):
    """
    The parent class for entities, it initializes the entities position, level (height), and direction.
    Animations/sprites are also initialized if they exist.

    Entity.update(dir) updates the sprite's position, direction, and current frame (if animated)
    """
    def __init__(self, tile_size, flag=None, position=(0, 0), dimensions=None, sprites=None, updates_per_frame=1):
        """
        Creates basic Entity object, containing x, y position, direction, and sprites (if necessary)
        :param tile_size: integer tuple
        :param flag: string or None -- identifies what level to jump to
        :param position: integer tuple
        :param sprites: array of sprites
        :param updates_per_frame: integer indicating the number of position updates per sprite frame change
        :return: None
        """
        self.x = position[0] * tile_size[0]
        self.y = position[1] * tile_size[1]
        if dimensions is None:
            self.width = tile_size[0]
            self.length = tile_size[1]
        else:
            self.width = dimensions[0]
            self.length = dimensions[1]

        self.flag = flag
        self.dir = 2
        self.height = 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.length)

        if sprites:
            self.sprites = [[pygame.transform.scale2x(x) for x in y] for y in sprites]
            self.frames = len(self.sprites)
            self.current_frame = 0
            self.current_sprite = self.sprites[self.dir][self.current_frame]
            self.updates_per_frame = updates_per_frame
            self.update_counter = 0

    def update(self, direction=None, force_update=False):
        """
        Updates current sprite (in animation cycle) and direction of sprite
        :param direction: The direction of sprite: 0: N, 1: E, 2: S, 3: W
        :return: None
        """
        self.update_counter += 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.length)

        if force_update:
            self.update_counter = self.updates_per_frame

        if direction is not None:
            self.dir = direction

        if self.update_counter == self.updates_per_frame:
            self.update_counter = 0
            self.current_frame = (self.current_frame + 1) % (self.frames)
            self.current_sprite = self.sprites[self.dir][self.current_frame]


class Player(Entity):
    """
    The Player class contains additional variables and sprites.
    """

    def __init__(self):
        """
        Initializes the entity at no position in particular -- placing is done by the level
        """
        player_sheet = tools.SpriteSheet('resources/player.png').get_sheet((0, 0, 16, 16), 8, 3)
        sprite_list = [player_sheet[0][:4], player_sheet[1][4:], player_sheet[0][4:], player_sheet[1][:4]]

        Entity.__init__(self, tile_size=(32, 32), sprites=sprite_list, updates_per_frame=6)


class Door(Entity):
    """
    The Door class is invisible, and serves only to detect if the place has collided with it.
    It is a 1px tall horizontal line at the top of the Door boundary
    """
    def __init__(self, position, flag):
        Entity.__init__(self, (32, 32), flag=flag, position=position, dimensions=(32, 9), updates_per_frame=1)
