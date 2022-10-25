#  #Iteration 1 - Core
# Character 


#  - Name - a string, something obnoxious and medevial

#  - Alignment - alignment chart - an array? Objects?

#  - Armor Class and Hit points - health - integers

#  - Can Attack - function() that gives damage to other characters or NPCs
#   - Need value of opponents armor class
#   - *stretch* may want strength of attack to differ based on strength and weapon of character
#   - double damage if a 20 is rolled
#   - character can gain experience when attacking
#    successful attack gives character 10 xp

#  - Can be damaged - function() 
#   - inverse of the can attack function()

#  - Abilities - object with key- value pairs
#   - Add modifiers for abilities

#  - Levels
#   - increments level after each 1000xp
#   - for each level hit points increase by 5 (+ Con modifier)
#   - +1 to attack points for every even level