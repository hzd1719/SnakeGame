import random

import pygame
from pygame import mixer

import sys

def snake_and_fruit(snake, fruit, ai_settings):
    #What happends when tha snake eats the fruit
    
    if snake.rect.colliderect(fruit.rect):
        #If there is music I lower it and play eating sound
        mixer.music.set_volume(0.1)
        mixer.music.pause()
        apple_sound = mixer.Sound("music/apple_sound4.wav")
        apple_sound.play()

        #New spawn point for the fruit
        fruit.rect.x =  random.randint(30, ai_settings.screen_width-30)
        fruit.rect.y =  random.randint(30, ai_settings.screen_height-30)

        for x in snake.snake_list[:-1]:
            while fruit.rect.x == x[0] or fruit.rect.y == x[1]:
                fruit.rect.x =  random.randint(30, ai_settings.screen_width-30)
                fruit.rect.y =  random.randint(30, ai_settings.screen_height-30)


        fruit.x = float(fruit.rect.x)
        fruit.y = float(fruit.rect.y)

        snake.length_snake += 2  #How fast the snake grows
        ai_settings.score += 1   #Increase the score
        ai_settings.snake_speed += 0.1
        mixer.music.unpause()
        mixer.music.set_volume(0.5)

def score(ai_settings, screen):
    #Display score function
    value = ai_settings.score_font.render("Score: " + str(ai_settings.score), True, ai_settings.score_color)
    screen.blit(value, [10, 10])

def message(msg, color,ai_settings, screen,w ,h):
    #Display message function 
    mesg = ai_settings.message_style.render(msg, True, color)
    screen.blit(mesg, [ai_settings.screen_width / w, ai_settings.screen_height / h])

def menu(ai_settings, screen, background_ps, play_button):
    while ai_settings.game_over == True:
        #mixer.music.rewind()
        screen.fill(ai_settings.before_color)
        screen.blit(background_ps.image, background_ps.rect)
       

        play_button.draw_button()
        #gf.score(ai_settings, screen)     #Optional Score while in the menu
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_p:
                    ai_settings.game_over = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(mouse_x, mouse_y):
                    ai_settings.game_over = False
            elif event.type == pygame.QUIT:
                sys.exit()
