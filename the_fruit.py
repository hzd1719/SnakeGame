import pygame

import random

class Fruit:
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/apple.png').convert_alpha()
        
        self.randomize(ai_settings)
        

    def draw_fruit(self, ai_settings):
        """Draw the apple at its current location."""
        self.rect = pygame.Rect(int(self.pos_x * ai_settings.cell_size),int(self.pos_y * ai_settings.cell_size),ai_settings.cell_size,ai_settings.cell_size)
        self.screen.blit(self.image, self.rect)
    
    def randomize(self, ai_setttings):
        self.pos_x =  random.randint(0, ai_setttings.cell_number_w - 1)
        self.pos_y =  random.randint(0, ai_setttings.cell_number_h - 1)
    
        
		

