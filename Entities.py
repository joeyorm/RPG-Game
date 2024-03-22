from entity_properties import *
import pygame

class Entity:
    def __init__(self, name): 
        #Core Attributes
        self.pos_xy = (0,0)
        self.sprite_sheet = None
        self.collision_box = (10,10)
        
        #Movement Attributes
        self.velocity_x = 0
        self.facing_direction = None #right left 
        
        #Gameplay Attributes
        self.health = 100
        self.attack_power = 1
        self.defense = 0
        self.state = None #idle, attacking, moving, dead
        self._name = name
        self.lvl = 0
        self.exp = 0
        self.dead = False 
        self.speed = 1
        self.inventory = []
        
        
        
    def take_damage(self):
        self.health -= self.attack_power
        if self.health <= 0:
            self.dead = True
            self.state = dead
            print(f'{self.name} has been defeated!')
            
    def attack(self, enemy):
        enemy.take_damage(self.attack_power)
        print(f'{self.name} has attacked!, {enemy.name} has {enemy.health} left.')