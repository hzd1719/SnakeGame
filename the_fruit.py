import pygame

import random

class Fruit:
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/apple5.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x =  random.randint(50, ai_settings.screen_width-50)
        self.rect.y =  random.randint(30, ai_settings.screen_height-30)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the apple at its current location."""
        self.screen.blit(self.image, self.rect)

