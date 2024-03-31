from Entities.Player import *
import pygame

# pygame.init()

# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("My RPG")

# start_img = pygame.image.load('').convert_alpha()
Steve = Player('steve')
Zombie = Player('zombie')



run = True
while run:
    
    print('\n')
    action = input('What is your action: ')
        
    Steve.EntityUpdate()
    # pygame.display.flip()
    
# pygame.quit()