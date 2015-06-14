import pygame

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
