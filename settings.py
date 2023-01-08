import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.cell_size = 40
        self.cell_number_w = 15
        self.cell_number_h = 15
        self.screen_width = self.cell_size * self.cell_number_w
        self.screen_height = self.cell_size * self.cell_number_h
        self.bg_color = (126,200,80) #Green
        
        # Snake settings
        self.snake_color = 0, 0, 0 #Black
        self.snake_width = self.cell_size
        self.snake_height = self.cell_size
        self.snake_speed = 10
        
        #Score settings
        self.score = 0
        self.score_font = pygame.font.SysFont("comicsansms", 20)
        self.score_color = (255, 255, 255) #White
        self.message_style = pygame.font.SysFont("bahnschrift", 35)
        self.message_color = (255, 0, 0)

        #Menu settings
        self.before_color = (255, 255, 255)


        self.game_over = True

    

