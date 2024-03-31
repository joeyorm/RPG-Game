from Entity import Entity

class Player(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.attack_power = 8
        self.speed = 4
    
        