from character import Char

# Is Class Character empty/ None?
# Test should Pass with param of str for self.name 
def test_character_class():
    assert not Char('name') == None


#Does Character() class have a name? self.name = ""
# Test should pass
def test_char_name():
    char = Char("name")
    assert not char.name == None


# Check that character alignment is = "neutral"
def test_char_align():
    garth = Char('garth')
    assert garth.align == 'neutral' or 'good' or 'evil'
    

# Is the default value of armor_class equal to 10 int
def test_armor_init_value():
    arm = Char("arm")
    assert arm.armor == 10

# Is the default hit point value equal to 0
def test_hp_init_value():
    brian = Char('brian')
    assert brian.hit_points == 5

# Is the default experience (xp) equal to 0
def test_xp_init():
    joe = Char("joe")
    assert joe.xp == 0

# check inital level of character
def test_level_init():
    bob = Char('bob')
    assert bob.level == 1

# check default attack_value is equal to 1 
def test_attack_value():
    tom = Char('tom')
    assert tom.attack_value == 1

# confirm init abilities value is set to 10
def test_abilities_init_values():
    gary = Char('gary')
    for value in gary.abilities.values():
        assert value == 10

def test_modifier_tuple_length():
    jon = Char('jon')
    assert len(jon.modifier_list) == 20

# test checks that each modifer in list has a value
def test_modifer_list_values():
    jon = Char('jon')
    for i in range(len(jon.modifier_list)):
        assert jon.modifier_list[i] != None

# Current modifier cmod has a value of 0 

def test_cmod_value():
    dan = Char('dan')
    assert dan.modifier == 0

def test_modify_method():
    carl = Char('carl')
    carl.__mod__("dexterity",19)
    assert carl.modifier == 4

def test_abilities_modifiers():
    dan = Char('dan')
    dan.__mod__('strength', 2)
    assert dan.abilities['strength'] == 6

#  Attack Method

# Does Attack method increase self.xp by 10
def test_attack_method():
    dan = Char('dan')
    jon = Char('jon')
    dan.attack(12,jon)
    assert dan.xp == 10
# Does opp (jon) hit_points decrease by dan.attack_value default (1)
def test_attack_on_opp():
    dan = Char('dan')
    jon = Char('jon')
    dan.attack(12, jon)
    assert jon.hit_points == 4
    
# Does attack_value double if a roll is greater than 19
def test_double_attack():
    dan = Char('dan')
    jon = Char('jon')
    dan.attack(20,jon)
    assert jon.hit_points == 3

# Does roll equal or is greater than opp(jon).armor then sub opp.hit_points - self(dan).attack_value
def test_hit_attack():
    dan = Char('dan')
    jon = Char('jon')
    dan.attack(15,jon)
    assert jon.hit_points == 4 

# Does opp(jon) hit_points stay at 5 if a roll is below opp(jon).armor
def test_miss_attack():
    dan = Char('dan')
    jon = Char('jon')
    dan.attack(8,jon)
    assert jon.hit_points == 5

def test_attack_outcomes():
    dan = Char('dan')
    jon = Char('jon')
    dan.attack(12, jon)
    assert dan.xp == 10 and jon.hit_points == 4

def test_attack_outcomes_miss():
    dan = Char('dan')
    jon = Char('jon')
    dan.attack(4, jon)
    assert dan.xp == 0 and jon.hit_points == 5

### 

### Check xp Method

# is xp incremented after a successful attack
def test_level_up_after_attack():
    dan = Char('dan')
    jon = Char('jon')
    for x in range(100):
        dan.attack(10, jon)
        
    assert dan.level == 2 and dan.xp == 0

# Does xp reset to 0 once it hits 1000 or greater

# Does level increase by one evertime xp is greater then 999

# Does HP increase by +5 every time xp is greater then 999

# Does attack_value increase by 1 everytime xp 999
 