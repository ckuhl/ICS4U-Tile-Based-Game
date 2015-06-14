import pygame
import tools.spritesheet

def fade(resolution, darkness):
    """
    Creates a transparent surface to overlay on the screen for fading effects.
    :param resolution: integer tuple -- (width, height) of the screen
    :param darkness: integer -- the darkness to set the screen (range: 0 - 64)
    :return:
    """
    fader_surface = pygame.Surface(resolution)
    fader_surface.fill((0, 0, 0))
    fader_surface.set_alpha(darkness * 16)
    return fader_surface


class MainMenu(object):
    def __init__(self):
        self.background = pygame.image.load('resources/menu_base.png')
        self.background = pygame.transform.scale2x(self.background)

        button_sheet = tools.spritesheet.SpriteSheet('resources/menu_buttons.png').get_line((0, 0, 19, 22), 2)

        self.start_button = pygame.transform.scale2x(button_sheet[0])
        self.start_pos = (50, 330)
        self.start_rect = pygame.Rect(self.start_pos, (38, 44))

        self.quit_button = pygame.transform.scale2x(button_sheet[1])
        self.quit_pos = (292, 330)
        self.quit_rect = pygame.Rect(self.quit_pos, (38, 44))


def draw_text(string):
    """
    Given an inputted score, constructs the score out of sprites
    :param string: integer -- high score
    :return: pygame.Surface -- the high score in sprites
    """
    text_sheet = tools.spritesheet.SpriteSheet('resources/font.png').get_sheet((0, 0, 7, 11), 13, 7)
    string = str(string)

    # the value of each character in the spritesheet
    relations = {'A':  0, 'a':  1, 'B':  2, 'b':  3, 'C':  4, 'c':  5, 'D':  6, 'd':  7, '1':  8, '2':  9, '3': 10,
                 '4': 11, '5': 12, 'E': 13, 'e': 14, 'F': 15, 'f': 16, 'G': 17, 'g': 18, 'H': 19, 'h': 20, '6': 21,
                 '7': 22, '8': 23, '9': 24, '0': 25, 'I': 26, 'i': 27, 'J': 28, 'j': 29, 'K': 30, 'k': 31, 'L': 32,
                 'l': 33, '#': 34, '!': 35, '?': 36, ',': 37, '.': 38, 'M': 39, 'm': 40, 'N': 41, 'n': 42, 'O': 43,
                 'o': 44, 'P': 45, 'p': 46, 'Q': 52, 'q': 53, 'R': 54, 'r': 55, 'S': 56, 's': 57, 'T': 58, 't': 59,
                 'U': 65, 'u': 66, 'V': 67, 'v': 68, 'W': 69, 'w': 70, 'X': 71, 'x': 72, 'Y': 78, 'y': 79, 'Z': 80,
                 'z': 81, ' ': 82}

    indexes = [relations[x] for x in string]

    number_sprites = [pygame.transform.scale2x(text_sheet[x // 13][x % 13]) for x in indexes]
    surface_width = 16 * len(string)

    score_surface = pygame.Surface((surface_width, 22), pygame.SRCALPHA)

    for n, i in enumerate(number_sprites):
        score_surface.blit(i, (n * 16, 0))

    return score_surface

