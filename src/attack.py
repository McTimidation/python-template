
class Attack:
    def __init__(self, roll, pred, opp):
        if roll >= opp.armor:
            pred.xp += 10
            self.check_xp(pred)
            if roll == 20:
                opp.hit_points -= (pred.attack_value * 2)
            else:
                opp.hit_points -= pred.attack_value
    def check_xp(self,pred):
        if pred.xp >= 1000:
            pred.level += 1
            pred.xp = 0
            pred.hit_points += 5
            if pred.level % 2 == 0:
                pred.attack_value += 1


# dan = Char('dan')
# jon = Char('jon')
# Attack(8,dan,jon)
# print(jon.hit_points)
# Attack(12, dan, jon)
# print(dan.xp, jon.hit_points)
# Attack(4, dan, jon)
# print(dan.xp, jon.hit_points)


