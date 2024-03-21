import pygame
class Entity:
    def __init__(self, name, health=100, dmg=15, lvl=1, x=10, y=10 ):
        
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

    
    def take_damage(self):
        self.health -= self.dmg
        if self.health <= 0:
            self.dead = True
            print(f'{self.name} has been defeated!')
            
    def attack(self, enemy):
        enemy.take_damage(self.dmg)
        print(f'{self.name} has attacked!, {enemy.name} has {enemy.health} left.')