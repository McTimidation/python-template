# class Ability:
#     SCORE_MODS = {
#         1: -5,
#         2: -4,
#         3: -4,
#         4: -3,
#         5: -3,
#         6: -2,
#         7: -2,
#         8: -1,
#         9: -1,
#         10: 0,
#         11: 0,
#         12: 1,
#         13: 1,
#         14: 2,
#         15: 2,
#         16: 3,
#         17: 3,
#         18: 4,
#         19: 4,
#         20: 5,
#     }
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         self.mod = Ability.SCORE_MODS[score]

#     def modify_score(self):
#         self.score -= 2

# class Char:
#     def __init__(self):
#         pass

#     def set_abilities(self, strength, wis, dex, const, char, intell):
#         self.strength = Ability('strength', strength)
#         self.wis = Ability('wis', wis)
#         self.dex = Ability('dex', dex)
#         self.const = Ability('const', const)
#         self.char = Ability('char', char)
#         self.intell = Ability('intell', intell)

# c = Char()
# print(c)
# c.set_abilities(1, 2, 3, 4 ,5 , 6)
# print(c.strength.score)

def shtuff(**kwargs):
    print(kwargs)
    for key in kwargs:
        print(key)
        print(kwargs[key])

shtuff(name='Jude', key='value', age="unknown")


  # loop through ablities object
        #      if we passed an ability as a kwarg for creation
        #            set attr to passed in value
        #     else
        #         set attr to default value from abilities