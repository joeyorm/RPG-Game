from Entity import Entity

class Player(Entity):
    def __init__(self, name, health, dmg, lvl):
        super().__init__(name, health, dmg, lvl)
        
    