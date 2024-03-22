import pygame
from Entities import Entity
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My RPG")

start_img = pygame.image.load('').convert_alpha()

run = True
while run:
    pygame.display.flip()
    
pygame.quit()