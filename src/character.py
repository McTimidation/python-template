
#Does Character() class have a name? self.name = ""
#

class Char:
    def __init__(self, name):
        self.name = name
        self.align= 'neutral'
        self.armor = 10
        self.hit_points = 0
        self.xp = 0
        self.level = 1
        self.attack_value = 1
        self.abilities = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "wisdom": 10,
            "intelligence": 10,
            "charisma": 10
        }

        