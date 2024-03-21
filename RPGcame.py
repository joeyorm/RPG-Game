import pygame
from Entities import Entity
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My RPG")

running = True

while running:
    pygame.display.flip()
    
pygame.quit()