import random

import pygame
from pygame import mixer

import sys

def snake_and_fruit(snake, fruit, ai_settings):
    #What happends when tha snake eats the fruit
    if snake.rect.colliderect(fruit.rect):
    #print(str(fruit.rect.x) + " compare to: " + str(snake.snake_list[-1][0]))
    #if fruit.rect.x == snake.snake_list[-1][0] or fruit.pos_y == snake.snake_list[-1][1]:
        #If there is music I lower it and play eating sound
        play_apple_sound()

        #New spawn point for the fruit
        fruit.randomize(ai_settings)

        for x in snake.snake_list[:-1]:
            if fruit.rect.x == x[0] or fruit.rect.y == x[1]:
                fruit.randomize(ai_settings)

        snake.length_snake += 1  #How fast the snake grows
        ai_settings.score += 1   #Increase the score
        #ai_settings.snake_speed += 0.1  
        mixer.music.unpause()
        mixer.music.set_volume(0.5)

def play_apple_sound():
    mixer.music.set_volume(0.1)
    mixer.music.pause()
    apple_sound = mixer.Sound("music/apple_sound4.wav")
    apple_sound.play()

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
