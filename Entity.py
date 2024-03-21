import pygame
class Entity:
    def __init__(self, name, health=100, dmg=15, lvl=1 ):
        self.action_sprites = {}
        self.current_action = "idle" 
        self.current_frame = 0  
        self.rect = self.rect = pygame.Rect(100, 50, 32, 32)
        self.speed = 10
        
        self._name = name
        self.health = health
        self.dmg = dmg
        self.lvl = lvl
        self.dead = False
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def health(self):
        return self.health
    @health.setter
    def health(self, value):
        if value < 0:
            self.health = 0
        else:
            self.health = value
    
    @property
    def dmg(self):
        return self.dmg
    @dmg.setter
    def dmg(self, value):
        self.dmg = value
        
    @property
    def lvl(self):
        return self.lvl
    @lvl.setter
    def lvl(self, value):
        self.lvl = value
    
    @property
    def dead(self):
        return self.dead
    @dead.setter
    def dead(self, value):
        self.dead = value
    
    @property
    def speed(self):
        return self.speed
    @speed.setter
    def speed(self, value):
        self.speed = value
        
    def load_and_split_sprite_sheet(self, filename, num_frames):
        spritesheet = pygame.image.load(filename).convert_alpha()  
        frames = []
        width = spritesheet.get_width() // num_frames 
        for i in range(num_frames):
            frame_rect = (i * width, 0, width, spritesheet.get_height())
            frames.append(spritesheet.subsurface(frame_rect))
        return frames
    
    def load_sprites(self, action_name, sprite_sheet):
        self.action_sprites[action_name] = self.load_and_split_sprite_sheet(sprite_sheet, 1)
        
    def update(self):  
        self.handle_animation()
        self.handle_movement() 

    def handle_animation(self):
        self.current_frame += 1
        if self.current_frame >= len(getattr(self, f"images_{self.current_action}")):
            self.current_frame = 0
        self.image = getattr(self, f"images_{self.current_action}")[self.current_frame]
    
    def handle_movement(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed  
    
    def take_damage(self):
        self.health -= self.dmg
        if self.health <= 0:
            self.dead = True
            print(f'{self.name} has been defeated!')
            
    def attack(self, enemy):
        enemy.take_damage(self.dmg)
        print(f'{self.name} has attacked!, {enemy.name} has {enemy.health} left.')