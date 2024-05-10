#!/usr/bin/env python

'''This is my first portfolio project from Codecademy. I am going to create a very simple text based
dungeon crawl where the player will be able to select their name. They will start with a small back
story and then they will be able to explore, encounter enemies, fight, flee, heal, and shop. There
will be a simple inventory management system.
A more detailed outline can be found within Notes.py'''

__author__      = "John W. Davis"
__copyright__   = "2024 - The Codecademy Project"
__credits__     = ["John W. Davis"]
__license__     = ""
__version__     = "0.0.1"
__maintainer__  = "John W. Davis"
__email__       = "ElectricViper@VipersByteSolutions.com"
__status__      = "Prototype" #"Development" | "Production"

from asyncio.windows_events import NULL
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')

print("""
      Welcome adventurer! Welcome to your final days. You have become the latest test subject of
      the mad wizard Professor Bon Von Jovian  
      
      You have awoken in a cold, dark room.
      The only sound is that of the dripping of water in the distance.
      As your vision clears and you shake the cobwebs from your head, you begin
      to recall the events leading up to this point. You were at an office party when 
      you started to feel ill. You remember someone claiming to be a doctor had offered
      to help you. Your world faded to black after accepting her help.
      
      You snap out of your thoughts as a very large rat scurries across the floor and over
      your leg eliciting a small yelp from you.
      """)

input("Press 'Enter' when you are ready to move on.")

print("""\n
      As you look around the room you see that you are in a small rectangular room
      made with rough stone walls and at one time it looks to have been a pantry. As you
      investigate the pantry, you realize that you are only wearing some very basic
      garments. No, make that more like dirty rags. What'ev, as you look around the room
      you find and old chef's knife. No sooner have you picked up the knife that you hear
      the squeeking of an ROUS or Rodents of Unusual Size. In laymen's terms ... a giant rat!
      
      Prepare to fight, because one of you two is on the menu for supper tonight.
      And I don't think that you want it to be you that's on the dinner menu.
      """)

input("Remember to just breathe. When you have collected your thoughs, press 'Enter' to continue.\n\n")

name = input("What is your name, brave soul?\nIf you don't answer, I will pick one for you:   ")
if not name:
    name = "Soandso"
gender = input("What gender do you identify as?\nIf you don't pick one, I'll set you as 'Neutral':   ")
if not gender:
    gender = "Neutral"
race = "Human"

class PlayerCharacter:

    def __init__(self, name, gender, race, strength = 10, dexterity = 10, constitution = 10, alive = True):
        self.name = name 
        self.gender = gender
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.level = 1
        self.experience = 0
        self.alive = alive
        self.weapon = "Rusty Kitchen Knife"
        self.armor_upper_body = "Rags"
        self.armor_lower_body = "Rags"

    def __repr__(self):
        return f'PlayerCharacter("All you know is that you are a {self.gender} {self.race} and you think that your name is "{self.name}"\nYou think that is your name at least.)'
    
    def attack(self, attack_rating, damage):
        self.attack_rating = attack_rating
        self.damage = damage

    def check_inventory():
        pass

    def quaff_potion():
        pass

    def move():
        pass

    def open():
        pass


#This is the dictionary of weapons, armor, potions and monsters.
# "Weapon name": Damage value
dict_weapons = {"Rusty Kitchen Knife": 5, "Shortsword": 10, "Longsword": 15, "Greatsword": 20}
# "Armor name": [Defence value, cost]
dict_armors = {"Rags": [0, 0], "Cloth Armor": [1, 10], "Leather Armor": [3, 25], "Chainmail": [6, 70], "Platemail": [ 8, 200]}
# "Healing potion name": [Healing value, cost].
dict_potions = {"Potion of healing": [30, 15], "Elixir of healing": [60, 40], "Infustion of healing": [120, 100], "Tincture of healing": [300, 250]}
# {"Monster Name": [hitpoints, attack_rating, damage, armor_rating, experience_value, gold multiplier, alive]}
# The gold multiplier is to reduce or increase the value earned based on the creatures difficutly.
dict_monsters = {"ROUS": [5, 4, 3, 4, 7, 0.7, True]}


class Monster:
    # The goal here is to have a single monster class and it can be populated with various monsters
    # from the dictionary to provide unique monsters.
    def __init__(self, name, hitpoints, attack_rating, damage, armor_rating, experience_value, gold_multiplier, alive):
        self.name = name
        self.hitpoints = hitpoints
        self.attack_rating = attack_rating
        self.damage = damage
        self.armor_rating = armor_rating
        self.experience_value = experience_value
        self.gold_multiplier = gold_multiplier
        self.alive = True

# Main code below here.

hero_pc = PlayerCharacter(name, gender, race)

to_hit_dice = random.randint(1, 20)
damage_dice = random.randint(1, 8)
# Testing random number generator
for i in range(0, 10):
    damage_dice = random.randint(1, 8)
    print(f"Random damage die rolls: {damage_dice} + 1 = " + str((damage_dice + 1)))

# This section is just for testing to make sure that the fields are being properly set.
print(hero_pc.name)
print(hero_pc.race)
print(hero_pc.gender)
print(hero_pc.strength)
print(hero_pc.dexterity)
print(hero_pc.constitution)
print(hero_pc.level)
print(hero_pc.experience)
# This is the end of the testing section for the entries for the PlayerCharacter class.

goodbye = input("Press enter to exit.")