import pygame
import tools.spritesheet

class HudOverlay(object):
    def __init__(self):
        """
        Creates the base HUD to print on the screen
        :return: None
        """
        self.ui_sheet = tools.spritesheet.SpriteSheet('resources/ui_hud.png').get_sheet((0, 0, 8, 16), 16, 6)
        self.overlay = pygame.Surface((511, 32))
        print(type(self.overlay))
        money_base = [26, 27, 34, 35, 27, 0, 1, 0, 1, 0, 1, 0, 1, 27, 28]
        health_base = [26, 27, 38, 39, 27, 74, 74, 74, 74, 74, 74, 74, 74, 27, 28]

        money_sprites = [pygame.transform.scale2x(self.ui_sheet[x // 16][x % 16]) for x in money_base]
        health_sprites = [pygame.transform.scale2x(self.ui_sheet[x // 16][x % 16]) for x in health_base]

        for n, i in enumerate(money_sprites):
            self.overlay.blit(i, (16 * n, 0))

        for n, i in enumerate(health_sprites):
            self.overlay.blit(i, (256 + 16 * n, 0))

    def update_money(self, value):
        """
        Creates a Surface containing the current amount of money the player has.
        :param value: integer -- amount of money
        :return: pygame.Surface
        """
        numbers = {'0': [ 0,  1], '1': [ 2,  3], '2': [ 4,  5], '3': [ 6,  7], '4': [ 8,  9],
                   '5': [16, 17], '6': [18, 19], '7': [20, 21], '8': [22, 23], '9': [24, 25]}

        if value > 9999:
            value = 9999
        value = str(value)
        while len(value) < 4:
            value = '0' + value

        number_overlay = pygame.Surface((128, 32))
        nums_base = []

        for i in value:
            nums_base += numbers[i]
        nums_sprites = [pygame.transform.scale2x(self.ui_sheet[x // 16][x % 16]) for x in nums_base]

        for n, i in enumerate(nums_sprites):
            number_overlay.blit(i, (16 * n, 0))

        return number_overlay

    def update_health(self, value):
        """
        Creates a surface object representing the amount of health the player has.
        :param value: integer -- amount of health the player has (range 0 - 16)
        :return: pygame.Surface
        """
        health_bar_base = []
        health_overlay = pygame.Surface((128, 32))

        while value:
            if value > 1:
                health_bar_base.append(11)
                value -= 2
            elif value == 1:
                health_bar_base.append(12)
                value -= 1

        healthbar_sprites = [pygame.transform.scale2x(self.ui_sheet[x // 16][x % 16]) for x in health_bar_base]

        for n, i in enumerate(healthbar_sprites):
            health_overlay.blit(i, (16 * n, 0))

        return health_overlay