import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 500
        self.bg_color = (126,200,80) #Green
        
        # Snake settings
        self.snake_color = 0, 0, 0 #Black
        self.snake_width = 15
        self.snake_height = 15
        self.snake_speed = 9
        
        #Score settings
        self.score = 0
        self.score_font = pygame.font.SysFont("comicsansms", 20)
        self.score_color = (255, 255, 255) #White
        self.message_style = pygame.font.SysFont("bahnschrift", 35)
        self.message_color = (255, 0, 0)

        #Menu settings
        self.before_color = (255, 255, 255)


        self.game_over = True

    

