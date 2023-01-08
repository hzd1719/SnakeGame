import pygame
import game_functions as gf

from settings import Settings
from the_snake import Snake
from the_fruit import Fruit
from button import Button
from background import Background_pause
from background import Background_game
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
snake = Snake(ai_settings)
fruit = Fruit(ai_settings, screen)

clock = pygame.time.Clock()


background_game = Background_game("images/new_turf.jpg", [0][0])
background_ps = Background_pause("images/snake_bg6b6.png", [0][0])
play_button = Button(screen, "Play")
pygame.display.set_caption("Snake Game")
#game_over = True

mixer.music.load("music/snake_song.mp3")
mixer.music.play(loops = -1, start = 5)
mixer.music.set_volume(0.5)


#pygame.mixer.Channel(0).play(pygame.mixer.Sound("music/snake_song.mp3"))
#pygame.mixer.Channel(1).play(pygame.mixer.Sound('music\game_over.mp3'))

while True:
    
    mixer.music.rewind()
    gf.menu(ai_settings, screen, background_ps, play_button)
     
    snake.move_snake(ai_settings)
    snake.in_game_logic(ai_settings, screen, fruit)
    
    screen.fill(ai_settings.bg_color)
    screen.blit(background_game.image, background_game.rect)
    gf.score(ai_settings, screen)
    fruit.draw_fruit(ai_settings)
    
    
    snake.snake_update(ai_settings,screen, fruit)
    snake.draw_snake(screen, ai_settings)
    
    
    pygame.display.update()
    
    gf.snake_and_fruit(snake, fruit, ai_settings)
    
    
    clock.tick(30)


