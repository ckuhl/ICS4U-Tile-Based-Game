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
