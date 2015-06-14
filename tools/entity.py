import pygame
import tools.spritesheet


class Entities(object):
    def __init__(self, entity_file, player, tile_size):
        """
        Populates a list of entities from the entities file
        :param entity_file: string -- the file to read entities from
        :return: None
        """
        self.entity_list = []
        self.player = player

        with open(entity_file, 'r') as file:
            for line in file:
                arguments = line.strip().split()
                entity_id, pos, height = arguments[0], (int(arguments[1]), int(arguments[2])), int(arguments[3])
                try:
                    flag = arguments[4]
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
            self.player.pos[0], self.player.pos[1] = pos[0] * tile_size[0], pos[1] * tile_size[1]
            return False
        elif entity_id == 'D':
            return Door(pos, flag)
        elif entity_id == 'C':
            return Coin(pos, flag)
        elif entity_id == 'S':
            return Sneeb(pos, flag)
        else:
            raise KeyError

    def kill(self, entity_to_remove):
        self.entity_list.remove(entity_to_remove)

    def collisions(self):
        return [self.entity_list[y] for y in self.player.hitbox.collidelistall([x.hitbox for x in self.entity_list])]

class Entity(object):
    """
    The parent class for entities, it initializes the entities position, level (height), and direction.
    Animations/sprites are also initialized if they exist.

    Entity.update(dir) updates the sprite's position, direction, and current frame (if animated)
    """
    def __init__(self, tile_size, height=1, flag=None, tile_pos=(0, 0), hitbox=None, direction=0):
        """
        Creates the basic entity object, containing the tile size, position, hitbox, and direction (if it exists)
        :param tile_size: integer tuple -- (height, width) of a single tile
        :param height: integer -- the height at which an entity exists
        :param flag: string -- a flag to indicate where a Door should warp to
        :param tile_pos: integer tuple -- (x, y) of where the tile exists on a grid map
        :param hitbox: integer 4-tuple -- (x-offset, y-offset, x-width, y-height) of the hitbox, from the tile position
        :param direction: integer -- direction of the object (0 if none, 1 north, 2 east, 3 south, 4 west)
        :return: None
        """
        self.tile_size = tile_size
        self.pos = [tile_pos[0] * tile_size[0], tile_pos[1] * tile_size[1]]
        self.hitbox_mod = hitbox
        if hitbox:
            self.hitbox = pygame.Rect((self.pos[0] + hitbox[0], self.pos[1] + hitbox[1], hitbox[2], hitbox[3]))
        else:
            self.hitbox = pygame.Rect(self.pos[0], tile_size)

        self.flag = flag
        self.height = height
        self.direction = direction
        self.health = float('inf')

        # sprite setup stuff
        self.current_frame = 0
        self.updates_per_frame = 0
        self.update_counter = 0
        self.frames = 0
        self.sprites = None
        self.current_sprite = None

    def set_sprites(self, sprites, updates_per_frame):
        """
        Sets the sprites for an object.
        :param sprites: list (or list of lists) of pygame.Surface
        :param updates_per_frame: integer -- the number of update calls to show each frame for
        :return: None
        """
        if self.direction:
            self.sprites = [[pygame.transform.scale2x(x) for x in y] for y in sprites]
            self.current_sprite = self.sprites[self.direction][self.current_frame]
        else:
            self.sprites = [pygame.transform.scale2x(x) for x in sprites]
            self.current_sprite = self.sprites[self.current_frame]

        self.frames = len(self.sprites)
        self.updates_per_frame = updates_per_frame
        self.update_counter = 0

    def update(self, direction=None, force_update=False):
        """
        Updates current sprite (in animation cycle) and direction of sprite
        :param direction: integer -- direction of sprite: 1 N, 2 E, 3 S and 4 W
        :return: None
        """
        self.update_counter += 1

        # update hitbox
        if self.hitbox_mod:
            self.hitbox = pygame.Rect((self.pos[0] + self.hitbox_mod[0], self.pos[1] + self.hitbox_mod[1], self.hitbox_mod[2], self.hitbox_mod[3]))
        else:
            self.hitbox = pygame.Rect((self.pos[0], self.pos[1], self.tile_size[0], self.tile_size[1]))

        if force_update:
            self.update_counter = self.updates_per_frame

        if self.direction:
            if direction is not None:
                self.direction = direction

        if self.update_counter == self.updates_per_frame:
            self.update_counter = 0
            self.current_frame = (self.current_frame + 1) % self.frames
            if self.direction:
                self.current_sprite = self.sprites[self.direction - 1][self.current_frame]
            else:
                self.current_sprite = self.sprites[self.current_frame]


class Player(Entity):
    """
    Creates the Player from Entity and a predefined spritesheet.
    Additional values are health and money.
    """
    def __init__(self):
        """
        Creates the player
        """
        player_sheet = tools.SpriteSheet('resources/player.png').get_sheet((0, 0, 16, 16), 8, 3)
        sprite_list = [player_sheet[0][:4], player_sheet[1][4:], player_sheet[0][4:], player_sheet[1][:4]]

        Entity.__init__(self, tile_size=(32, 32), hitbox=(4, 8, 24, 32), direction=2, )
        self.set_sprites(sprite_list, updates_per_frame=6)

        self.health = 16


class Door(Entity):
    """
    The Door class is invisible, and serves only to detect if the place has collided with it.
    It is a 1px tall horizontal line at the top of the Door boundary
    """
    def __init__(self, tile_pos, flag):
        Entity.__init__(self, (32, 32), flag=flag, tile_pos=tile_pos, hitbox=(8, 8, 32, 1))


class Coin(Entity):
    """
    The Coin class defines a coin.
    """
    def __init__(self, tile_pos, flag):
        coin_sheet = tools.SpriteSheet('resources/coins.png').get_sheet((0, 0, 16, 16), 8, 4)
        self.flag = flag

        if self.flag == 'small':
            sprite_list = coin_sheet[2][:4]
        else:
            sprite_list = coin_sheet[0][:4]

        Entity.__init__(self, tile_size=(32, 32), tile_pos=tile_pos, hitbox=(12, 20, 4, 4), flag=flag)

        self.set_sprites(sprites=sprite_list, updates_per_frame=12)
        self.health = 1
        self.pos[1] -= 10  # shift the sprite up (to the middle of a tile)

    def die(self):
        """
        Plays death sound effect.
        :return: None
        """
        death_sound = pygame.mixer.Sound('resources/coin.wav')
        death_sound.set_volume(0.3)
        death_sound.play()

class Sneeb(Entity):
    def __init__(self, tile_pos, flag):
        sneeb_sprite = pygame.image.load('resources/sneeb.png')
        self.flag = flag

        Entity.__init__(self, (32, 32), tile_pos=tile_pos, hitbox=(0, -16, 32, 32), flag=flag)
        self.current_sprite = sneeb_sprite
        self.pos[1] -= 8

    def die(self):
        death_sound = pygame.mixer.Sound('resources/coin.wav')
        death_sound.set_volume(0.6)
        death_sound.play()
