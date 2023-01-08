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
        self.apple_sound1 = mixer.Sound("music/mary_sound1.wav")
        
        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

        #to do:
        #1. snake speed trqbva da e 1 - taka shte se dviji ot kvadratche v kvadratche(zmiqta e 40 golqma kakto i kvadratcheto)
        #2. Da vidq zashto zmiqta mi stava defekta(raste na obratno) kogato speeda = 1, tova v update tail neshto - Nz
        #3. Da opravq blasknaeto na zmiqta v stenite - Done
        #4 da se spawnva po dalga zmiq

    def move_snake(self, ai_settings):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.x_change >= 0: #Move the snake only if it is not moving in the opposite direction
                    #apple_sound = mixer.Sound("music/mary_sound1.wav")
                    #self.apple_sound1.play()
                    self.x_change = ai_settings.snake_speed - 9
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
                    #self.apple_sound1.play()
                elif event.key == pygame.K_DOWN and self.y_change >= 0:
                    #apple_sound = mixer.Sound("music/mary_sound1.wav")
                    #self.apple_sound1.play()
                    self.y_change = ai_settings.snake_speed
                    self.x_change = 0
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        #print("self x.change: " + str(self.x_change)) self.x is rouned
        self.x = self.rect.x
        #print(self.x)
        self.y = self.rect.y

    def in_game_logic(self, ai_settings, screen, fruit):
        if len(self.snake_list) > 0:
            if self.snake_list[-1][0] < ai_settings.cell_number_w - ai_settings.snake_speed or self.snake_list[-1][1] < ai_settings.cell_number_h - ai_settings.snake_speed:
                self.reset(ai_settings, screen, fruit)
            elif self.snake_list[-1][0] > ai_settings.screen_width - (ai_settings.snake_width + ai_settings.snake_speed):
                self.reset(ai_settings, screen, fruit)
            elif self.snake_list[-1][1] > ai_settings.screen_height - (ai_settings.snake_height + ai_settings.snake_speed):
                self.reset(ai_settings, screen, fruit)
                

    def draw_snake(self, screen, ai_settings):
        self.update_snake_head()
        self.update_snake_tail(ai_settings)
        for i in range(len(self.snake_list)):
            block_rect = [self.snake_list[i][0], self.snake_list[i][1],
                ai_settings.snake_width, ai_settings.snake_height]
            
            if i == len(self.snake_list)-1:  #head
                screen.blit(self.img_head, block_rect)
            elif i == 0:  #tail
                screen.blit(self.img_tail, block_rect)
            else:  #body
                self.update_snake_body(i)
                screen.blit(self.img_body, block_rect)

                #pygame.draw.rect(screen, ai_settings.snake_color, [self.snake_list[i][0], self.snake_list[i][1],
                #ai_settings.snake_width, ai_settings.snake_height])


    def snake_update(self, ai_settings, screen, fruit):
        self.snake_head = []
        self.snake_head.append(self.x)
        self.snake_head.append(self.y)
        self.snake_list.append(self.snake_head)
        
        if len(self.snake_list) > self.length_snake:
            del self.snake_list[0]
 
        for x in self.snake_list[:-1]:
            if x == self.snake_head:
                self.reset(ai_settings, screen, fruit)
    
    def update_snake_head(self):
        self.img_head = self.head_right
        if self.x_change > 0 and self.y_change == 0:
                self.img_head = self.head_right
        elif self.x_change < 0 and self.y_change == 0:
                self.img_head = self.head_left
        elif self.x_change == 0 and self.y_change < 0:
                self.img_head = self.head_up
        elif self.x_change == 0 and self.y_change > 0:
                self.img_head = self.head_down
    
    def update_snake_tail(self, ai_settings):
        self.img_tail = self.tail_left
        if(len(self.snake_list ) > 1):
            #print(str(self.snake_list[0][0]) + " compare to X : " + str(self.snake_list[0+1][0]))
            #print(str(self.snake_list[0][1]) + " compare to Y : " + str(self.snake_list[0+1][1]))
            if self.snake_list[0][0] + ai_settings.snake_speed == self.snake_list[0+1][0]:
                    self.img_tail = self.tail_left
            elif self.snake_list[0][0] - ai_settings.snake_speed  == self.snake_list[0+1][0]:
                    self.img_tail = self.tail_right
            elif self.snake_list[0][1] + ai_settings.snake_speed == self.snake_list[0+1][1]:
                    self.img_tail = self.tail_up
            elif self.snake_list[0][1] - ai_settings.snake_speed  == self.snake_list[0+1][1]:
                    self.img_tail = self.tail_down
    def update_snake_body(self, i):
        self.img_body =  self.body_vertical
        prev_rect = (self.snake_list[i-1][0], self.snake_list[i-1][1])
        next_rect = (self.snake_list[i+1][0],self.snake_list[i+1][1])
        if prev_rect[0] == next_rect[0]:
            self.img_body =  self.body_vertical
        elif prev_rect[1] == next_rect[1]:
            self.img_body =  self.body_horizontal
        else:
            diff_prev_x = prev_rect[0] - self.snake_list[i][0]
            diff_prev_y = prev_rect[1] - self.snake_list[i][1]
            diff_next_x = next_rect[0] - self.snake_list[i][0]
            diff_next_y = next_rect[1] - self.snake_list[i][1]
                    
            if diff_prev_x == -10 and diff_next_y == -10 or diff_prev_y == -10 and diff_next_x == -10:
                self.img_body =  self.body_tl
            elif diff_prev_x == -10 and diff_next_y == 10 or diff_prev_y  == 10 and diff_next_x == -10:
                self.img_body =  self.body_bl
            elif diff_prev_x == 10 and diff_next_y  == -10 or diff_prev_y  == -10 and diff_next_x == 10:
                self.img_body =  self.body_tr
            elif diff_prev_x == 10 and diff_next_y == 10 or diff_prev_y == 10 and diff_next_x == 10:
                self.img_body =  self.body_br      

    def reset(self, ai_settings, screen, fruit):
        ai_settings.game_over = True
        ai_settings.score = 0
        gf.message("Game Over!", ai_settings.message_color, 
        ai_settings, screen, 2.5, 2.5)
        pygame.display.update()
        fruit.randomize(ai_settings)
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
        


