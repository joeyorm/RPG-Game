from entity_properties import *

class Entity:
    def __init__(self, name): 
        #Core Attributes
        self.pos_xy        = (0,0)
        self.sprite_sheet  = None
        self.collision_box = (0,0) #None 
        
        #Movement Attributes
        self.velocity         = 0
        self.facing_direction = None #right left 
        
        #Gameplay Attributes
        self.name         = name
        self.max_health   = 100
        self.health       = 100
        self.attack_power = 1
        self.lvl          = 1
        self.dead         = False 
        self.exp          = 0
        self.exp_lvl_up   = 50
        self.exp_drop     = 25
        self.speed        = 3
        self.defense      = 10
        self.state        = None #idle, attacking, moving, dead
        self.inventory    = []
        
    #UPDATE
    def calculate_stats(self):
        STANDARD_CONSTANT = (1.15 ** (self.lvl-1))
        self.lvl          = min(99, self.lvl)
        self.attack_power = min(99_999 , 8 * STANDARD_CONSTANT)
        self.max_health   = min(99_999 , 100 * STANDARD_CONSTANT)
        self.health       = min(99_999, self.health*STANDARD_CONSTANT)
        self.speed        = min(35, 3 * STANDARD_CONSTANT*1.05)
        self.defense      = min(99,999, 10 * STANDARD_CONSTANT)
        self.exp_lvl_up   = min(99,999, 50 * STANDARD_CONSTANT)
        self.exp          = min(99_999, self.exp)
        
    def check_level_up(self):
        if  self.exp >= self.exp_lvl_up:
            self.level_up()            
        return 
    
    #Functions
    def attack(self, enemy):
        enemy.health    -= self.attack_power
        
        if  enemy.health <= 0:
            enemy.health = 0
            enemy.dead   = True
            enemy.state  = "dead"
            self.exp    += enemy.exp_drop
            print(f'{enemy.name} has been defeated!')
        
        print(f'{enemy.name} has {enemy.health} left.')
    
    def heal(self, value = 15):
        self.health += value
        self.health = min(self.max_health, self.health)
    
    #admin functions
    def level_up(self, lvl=1):
        while self.exp >= self.exp_lvl_up:
            self.lvl   += lvl
            self.exp   -= self.exp_lvl_up
        
        print(f"{self.name} leveled up to level {self.lvl}")
    
    def EntityUpdate(self):
        self.check_level_up()
        self.calculate_stats()
        
    def print_stats(self):  
        stats = {
            "Level"  : self.lvl,
            "Damage" : round(self.attack_power),
            "Health" : round(self.health),
            "Exp"    : (f'{round(self.exp)}/{round(self.exp_lvl_up)}'),
            "Speed"  : round(self.speed),
            "Defense": round(self.defense),
        }
        
        for name, stat in stats.items():
            print(f"{name}: {stat}")
        
        