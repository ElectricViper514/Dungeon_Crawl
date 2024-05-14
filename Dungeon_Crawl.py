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
import time

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

os.system('cls' if os.name == 'nt' else 'clear')

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

input("Remember to just breathe. When you have collected your thoughs,\npress 'Enter' to continue.\n\n")

print("One more thing ...\n")
time.sleep(2)
print("The only way out is forward. You can go forward. You can go left. You can go even go right.\n\n")
time.sleep(2)
print("But you can never.")
time.sleep(2)
print("And I mean NEVER go back the way you came!\n\n")
nod_in_agreement = input("Let that sink into your little noodle.\nYou can nod your head in agreement by pressing enter\n\n")
time.sleep(2)
print("Take a breath, don't stress and remember ...")
time.sleep(2)
print("...\n\n")
time.sleep(2)
print("Do not say that ...\n\n")
time.sleep(2)
print("Yooouuuuu ...")
time.sleep(2)
print("Were ...\n\n")
time.sleep(1)
print("NOT ...\n\n")
time.sleep(2)
print("WARNED!!!\n\n")
time.sleep(2)
print("\n\n")

# Starting basic player stats.
player_stats = {"name": "Soandso", "gender": "Gender Nil", "race": "Human", "strength": 10, "dexterity": 10, "constitution": 10, "level": 1, "experience": 0, "alive": True}



'''name = input("What is your name, brave soul?\nIf you don't answer, I will pick one for you:   ")
if not name:
    name = "Soandso"'''

# Testing if Player Name and Gender are left blank. If they are then the default vaulue is used. If they enter something, then the player's entered value will be used in place of the default.
player_name = input("What is your name, brave soul?\nIf you don't answer, I will pick one for you:   ")
if len(player_name) == 0:
    print("\nYour name shall be set as 'Soandso'\nLet's move on the next question.")        
else:
    player_stats.update({"name": player_name})
    print(f"\n\nHello {player_name}.")

player_gender = input("\nWhat gender do you identify as?\n\nIf you don't pick one, I'll set you as 'Gender Nil':   ")
if len(player_gender) == 0:
    print("\nYour gender shall be set as 'Gender Nil'\nMoving on from the questions.\n")
else:
    player_stats.update({"gender": player_gender})

# Testing an alternative was of establishing a player. If this works then I can expand a different dictionary to create multiple types of monsters with the same class instead of having to create a new class for every monster type.

class Player:
    def __init__(self, player_stats):
        for key, value in player_stats.items():
            setattr(self, key, value)

player_equipment = {"weapon": "Rusty Kitchen Knife", "armor": "rags", "gold": 0}

test_player = Player(player_stats)
# This section is just for testing to make sure that the fields are being properly set.
print(f"Player's Name: {test_player.name}")
print(f"Player's Gender: {test_player.gender}")
print(f"Player's Race: {test_player.race}")
print(f"Player's Strength: {test_player.strength}")
print(f"Player's Desterity: {test_player.dexterity}")
print(f"Player's Constitution: {test_player.constitution}")
print(f"Player's Level: {test_player.level}")
print(f"Player's Experience: {test_player.experience}")
print(f"Player's Living Status: {test_player.alive}")

'''class PlayerCharacter:

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
        self.armor = "Rags"

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
'''

#This is the dictionary of weapons, armor, potions and monsters.
# Stats and their bonuses
dict_stat_bonues = {2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10}

# "Weapon name": Min Damage, Max Damage, Cost
dict_weapons = {"Rusty Kitchen Knife": [1, 4, 1], "Shortsword": [1, 6, 10], "Longsword": [1, 8, 20], "Greatsword": [2, 12, 50]}

# "Bonus Damage: -5 through +5"
dict_damage_modifier = {"Crippling": -5, "Debilitating": -4, "Weakening": -3, "Hampering": -2, "Slight Impairment": -1, "Normal": 0, "Slight Enhancement": 1, "Boosting": 2, "Strengthening": 3, "Empowering": 4, "Potent": 5}

# "Armor name": [Defence value, cost]
dict_armors = {"Rags": [0, 0], "Cloth Armor": [1, 10], "Leather Armor": [3, 25], "Chainmail": [6, 70], "Platemail": [ 8, 200]}

# "Healing potion name": [Healing value, cost].
dict_potions = {"Potion of healing": [30, 15], "Elixir of healing": [60, 40], "Infustion of healing": [120, 100], "Tincture of healing": [300, 250]}

# {"Monster Name": [hitpoints = 5, to hit modifier = 1, max damage = 3, defence bonus = 4, experience_value = 7, max gold = 3, alive = True]}
dict_monsters = {1: "Giant Rat", 2: "Goblin", 3: "Kobold"}
dict_giant_rat = {"name": "Giant Rat", "hit_points": 7, "to_hit": 4, "damage": 3, "defense_rating": 2, "experience_value": 25, "gold": 3, "is_alive": True} # CR .125, HP = (2d6), Damage = ( 1d4 + 2)
dict_goblin = {"name": "Goblin", "hit_points": 7, "to_hit": 4, "damage": 5, "defense_rating": 2, "experience_value": 10, "gold": 5, "is_alive": True} # CR = .25, HP = (2d6), Damage = (2d6 + 2)
dict_kobold = {"name": "Kobold", "hit_points": 5, "to_hit": 4, "damage": 3, "defense_rating": 2, "experience_value": 25, "gold": 7, "is_alive": True} # CR = .125, HP = (2d6 - 2), Damage = (1d4 + 2)

class Monster:
    def __init__(self, mob):
        for key, value in mob.items():
            setattr(self, key, value)

mob = {}
mob = dict_giant_rat

bob = Monster(mob)

#mob = {key: value for key, value in dict_monsters.items() if key.startswith("ROUS")}
#giant_rat = {}
#giant_rat = Monster(mob)

# filtered_dict = {key: value for key, value in my_dict.items() if key.startswith("ROUS")}

#print(f"Monster's Name: {giant_rat.startswith("ROUS")}")
#
# print(f"Monster's Race: {giant_rat.race}")

print("\n\nThis is the monster's stats\n\n")
print(f"Monster's Name: {(bob.name)}")
print(f"Monster's Hit Points: {bob.hit_points}")
print(f"Monster's To Hit Modifier: {bob.to_hit}")
print(f"Monster's Damage: {bob.damage}")
print(f"Monster's Defence Rating: {bob.defense_rating}")
print(f"Monster's Experience: {bob.experience_value}")
print(f"Monster's Gold: {bob.gold}")
print(f"Monster's Living Status: {bob.is_alive}")

# {"Monster Name": [0 hitpoints = 5, 1 to hit modifier = 1, 2 max damage = 3, 3 defence bonus = 4, 4 experience_value = 7, 5 max gold = 3, 6 alive = True]}
#dict_monsters = {"ROUS": [5, 1, 3, 4, 7, 3, True]}

'''class Monster:
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
        self.alive = True'''

# Main code below here.

#hero_pc = Player(name, gender, race)
# Random Dice Rollers

#to_hit_dice = random.randint(1, 20)
#damage_dice = random.randint(1, 8)
# Testing random number generator
#for i in range(0, 10):
    #damage_dice = random.randint(1, 8)
    #
    # print(f"Random damage die rolls: {damage_dice} + 1 = " + str((damage_dice + 1)))



# This is the end of the testing section for the entries for the PlayerCharacter class.

#
# goodbye = input("Press enter to exit.")