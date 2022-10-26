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
    assert brian.hit_points == 0

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


