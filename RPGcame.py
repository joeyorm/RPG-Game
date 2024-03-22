import pygame, sys
import spritesheet

pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RPG")

sprite_sheet_img = pygame.image.load("doux.png").convert_alpha()
spritesheet = spritesheet.SpriteSheet(sprite_sheet_img)

animation_list = []
animation_steps = [4,6,3,4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0
step_counter = 0


for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(spritesheet.get_image(step_counter, 24,24,3, (0,0,0)))
        step_counter += 1
    animation_list.append(temp_img_list)
    
run = True
while run:
                
    screen.fill((0,0,0))
    
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0
            
    screen.blit(animation_list[action][frame], (0, 0))    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) -1:
                action += 1
                frame = 0
            

    pygame.display.flip()
    clock.tick(60)