from Entity import *

class Enemy(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 2
        self.health = 20