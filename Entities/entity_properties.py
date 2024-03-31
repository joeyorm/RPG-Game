
#Core Attributes
@property
def pos_xy(self):
    return self.pos_x
@pos_xy.setter
def pos_xy(self, value):
    self.pos_xy = value
    
@property
def sprite_sheet(self):
    return self.sprite_sheet
@sprite_sheet.setter
def sprite_sheet(self, value):
    self.sprite_sheet = value

@property
def collision_box(self):
    return self.collision_box
@collision_box.setter
def collision_box(self, value):
    self.collision_box = value

#Movement Attribtes
@property
def velocity(self):
    return self.velocity
@velocity.setter
def velocity(self, value):
    self.velocity = value
    
@property
def facing_direction(self):
    return self.facing_direction
@facing_direction.setter
def facing_direction(self, value):
    self.facing_direction = value


#Gameplay Attributes
@property
def name(self):
    return self._name
@name.setter
def name(self, value):
    self._name = value

@property
def max_health(self):
    return self.max_health
@max_health.setter
def max_health(self, value):
    self.max_health = value

@property
def health(self):
    return self.health
@health.setter
def health(self, value):
    if value < 0:
        self.health = 0
    else:
        self.health = min(self.max_health, value)
  
@property
def attack_power(self):
    return self.attack_power
@attack_power.setter
def attack_power(self, value):
    self.attack_power = value
    
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
def exp(self):
    return self.exp
@exp.setter
def exp(self, value : int):
    self.exp = value
    
@property
def speed(self):
    return self.speed
@speed.setter
def speed(self, value):
    self.speed = value
    
@property
def defense(self):
    return self.defense
@defense.setter
def defense(self, value):
    self.defense = value
    
@property
def state(self):
    return state
@state.setter
def state(self, value):
    self.state = value
    
@property
def inventory(self):
    return self.inventory
@inventory.setter
def inventory(self, value = [], clear = False):
    if clear == True:
        self.inventory.clear()
    else:
        self.inventory = value
    
