
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
    ALIGNMENT = {'lawful good', 'lawful neutral', 'lawful evil', 'neutral good', 'true neutral', 'neutral evi', 'chaotic good', 'chaotic neutral', 'chaotic evil'}
    def __init__(self, name, **kwargs):
        self.name = name
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
        for a in Char.ALIGNMENT:
            if a in kwargs:
                self.align = a
            else:
                self.align = 'true neutral'
            



