
#Does Character() class have a name? self.name = ""
#

class Char:
    def __init__(self, name):
        self.name = name
        self.align= 'neutral'
        self.armor = 10
        self.hit_points = 5
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
        self.modifier_list = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
        self.modifier = self.modifier_list[10]

    def __mod__(self,score):
        mod_index = score - 1
        self.modifier = self.modifier_list[mod_index]

        
