
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
    ALIGNMENT = {
            'lawful_good': 'lawful good',
            'lawful_neutral': 'lawful neutral',
            'lawful_evil': 'lawful evil',
            'neutral_good': 'neutral good',
            'true_neutral': 'true neutral',
            'neutral_evil': 'neutral evil',
            'chaotic_good': 'chaotic good',
            'chaotic_neutral': 'chaotic neutral',
            'chaotic_evil': 'chaotic evil'}
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
                # print(a, 'a')
                # print(kwargs[a], 'kwA')
                
            else:
                value = Char.ABILITIES[a]
            setattr(self, a, Abilities(value))

        align = "true neutral"
        for a in Char.ALIGNMENT:
            if a in kwargs:
                align = Char.ALIGNMENT[a]
                print('align in if',align)

        setattr(self, 'align', align)
        print('self.align',self.align)
            

