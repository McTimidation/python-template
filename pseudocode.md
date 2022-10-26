# Requirements
This project is a collaboration with a partner about learning python, talking through pseudocode at a high level and mapping out courses of action to get there.

The hard requirements revolve around how many tests you can write and how many you can get to pass by then writing code for them. The goal is to get through two (2) iterations this week but since this is open ended do as much as you can.


To complete the assignment, you must complete the following:
1. Pseudocode should follow the examples and step through each individual task.
1. Code must be commented well.
1. Tests should be written first, then code written to pass the tests.
---

---

#  #Iteration 1 - Core
## Character - Python Class


- Name - a string, something obnoxious and medevial
    > SpaceBun The Great, Wizard of thee Space en shit

- Alignment - alignment chart - an array? Objects?
    > Array to organize the types of alignments and setAligment fn() and a var that holds Current_Alignment

- Armor Class and Hit points - health - integers
   > two vars int

- Can Attack - function() that gives damage to other characters or NPCs
   - Need value of opponents armor class
   - *stretch* may want strength of attack to differ based on strength and weapon of character
   - double damage if a 20 is rolled
   - character can gain experience when attacking
    successful attack gives character 10 xp

- Can be damaged - function() 
   - inverse of the can attack function()

- Abilities - object with key- value pairs
   - Add modifiers for abilities

- Levels
   - increments level after each 1000xp
   - for each level hit points increase by 5 (+ Con modifier)
   - +1 to attack points for every even level

---

