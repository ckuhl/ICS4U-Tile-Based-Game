import pygame

def fade_in(resolution, effect):
    fader_surface = pygame.Surface(resolution)
    fader_surface.fill((0, 0, 0))
    fader_surface.set_alpha(effect * 8)
    return fader_surface
