import pygame, sys

class Entity():
    def __init__(self, health, dmg, lvl = 0, exp = 0):
        self.health = health
        self.dmg = dmg
        self.lvl = lvl
        self.exp = exp

        
   