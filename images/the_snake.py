import pygame
import time
import sys
from pygame import mixer

import game_functions as gf

class Snake:
    def __init__(self, ai_settings):
        self.x = ai_settings.screen_width/2
        self.y = ai_settings.screen_height/2
        self.x_change = 0
        self.y_change = 0
        self.rect = pygame.Rect(self.x, self.y, ai_settings.snake_width,
        ai_settings.snake_height)
        self.snake_list = []
        self.length_snake = 1
        #self.apple_sound1 = mixer.Sound("music/mary_sound1.wav")
        

    def move_snake(self, ai_settings):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.x_change >= 0: #Move the snake only if it is not moving in the opposite direction
                    
                    #self.apple_sound1.play()
                    self.x_change = ai_settings.snake_speed
                    self.y_change = 0
                    
                elif event.key == pygame.K_LEFT and self.x_change <= 0:
                    #apple_sound = mixer.Sound("music/mary_sound1.wav")
                    #self.apple_sound1.play()
                    self.x_change = -ai_settings.snake_speed
                    self.y_change = 0
                    
                    
                elif event.key == pygame.K_UP and self.y_change <= 0:
                    self.y_change = -ai_settings.snake_speed
                    self.x_change = 0
                    #apple_sound = mixer.Sound("music/mary_sound1.wav")
                    #apple_sound.play()
                
                
                elif event.key == pygame.K_DOWN and self.y_change >= 0:
                    #apple_sound = mixer.Sound("music/mary_sound1.wav")
                    #apple_sound.play()
                    self.y_change = ai_settings.snake_speed
                    self.x_change = 0
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def in_game(self, ai_settings, screen):
        difficulty = "hard"
        if difficulty == "hard":
            #self.x += self.x_change
            if self.rect.x >= ai_settings.screen_width - 10:
                #self.rect.x = 0
                self.reset(ai_settings, screen)
            elif self.rect.x < 0 - 6:
                #self.rect.x = ai_settings.screen_width
                self.reset(ai_settings, screen)
            #self.y += self.y_change
            if self.rect.y >= ai_settings.screen_height - 6:
                #self.rect.y = 0
                self.reset(ai_settings, screen)
            elif self.rect.y < 0 - 5:
                #self.rect.y = ai_settings.screen_height
                self.reset(ai_settings, screen)

    def draw_snake(self, screen, ai_settings):
        for i in range(len(self.snake_list)):
            pygame.draw.rect(screen, ai_settings.snake_color, 
            [self.snake_list[i][0], self.snake_list[i][1], ai_settings.snake_width,
             ai_settings.snake_height])
            # x = snake_list[i][0]
            # y = snake_list[i][1]

    def snake_update(self, ai_settings, screen):
        self.snake_head = []
        self.snake_head.append(self.x)
        self.snake_head.append(self.y)
        self.snake_list.append(self.snake_head)
        if len(self.snake_list) > self.length_snake:
            del self.snake_list[0]
            
 
        for x in self.snake_list[:-1]:
            if x == self.snake_head:
                self.reset(ai_settings, screen)
                

    def reset(self, ai_settings, screen):
        ai_settings.game_over = True
        ai_settings.score = 0
        gf.message("Game Over!", ai_settings.message_color, 
        ai_settings, screen, 2.5, 2.5)
        pygame.display.update()
        self.x_change = 0
        self.y_change = 0
        self.rect.x = ai_settings.screen_width/2
        self.rect.y = ai_settings.screen_height/2
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.length_snake = 1
        self.snake_list.clear()
        mixer.music.pause()
        game_over_sound = mixer.Sound("music/game_over.wav")
        game_over_sound.play()
        time.sleep(2)
        mixer.music.unpause()
        


