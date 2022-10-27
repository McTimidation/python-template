
from abilities import Abilities
#Does Character() class have a name? self.name = ""
#

class Char:
    ABILITIES = {
        "strength": 10,
        "dexterity": 10,
        "constitution": 10,
        "wisdom": 10,
        "intelligence": 10,
        "charisma": 10
    }
    def __init__(self, name, **kwargs):
        self.name = name
        self.align= 'neutral'
        self.armor = 10
        self.hit_points = 5
        self.xp = 0
        self.level = 1
        self.attack_value = 1

        for a in Char.ABILITIES:
            if a in kwargs:
                value = kwargs[a]
            else:
                value = Char.ABILITIES[a]
            
            setattr(self, a, Abilities(value))



