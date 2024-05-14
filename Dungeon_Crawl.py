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

import os
import random
import time
from turtle import clear

os.system('cls' if os.name == 'nt' else 'clear')
clear

os.system('color')

text_bold = '\033[1m'
text_underline = '\033[4m'
text_invert = '\33[7m'
text_color_purple = '\033[95m'
text_color_blue = '\033[94m'
text_color_cyan = '\033[96m'
text_color_green = '\033[92m'
text_color_orange = '\033[93m'
text_color_red = '\033[91m'
text_end = '\033[0m'



print(text_color_blue + """
Welcome adventurer! Welcome to your final days. You have become the latest test subject of
the mad wizard Professor Bon Von Jovian  
      
You have awoken in a cold, dark room.
The only sound is that of the dripping of water in the distance.
As your vision clears and you shake the cobwebs from your head, you begin
to recall the events leading up to this point. You were at an office party when 
you started to feel ill. You remember someone claiming to be a doctor had offered
to help you. Your world faded to black after accepting her help.""" + text_end)

input("Press " + text_invert + "'Enter'" + text_end + " when you are ready to move on.")

print(text_color_green + """\n
As you look around the room you see that you are in a small rectangular room
made with rough stone walls and at one time it looks to have been a pantry. As you
investigate the supposed pantry, you realize that you are only wearing some very basic garments. No, make that more like dirty rags. What'ev ... as you look around the room you find an old chef's knife. While lost in thought wondering who would have left such a rusted piece of junk here you snap out of your thoughts as an 'R' 'O' 'U' 'S' or Rodent of Unusual Size scurries across the floor and up your leg eliciting a not so small yelping scream from you. You hear the juxting of the small teeth as the, 'R' 'O' 'U' ... in laymen's terms ... a giant rat prepares to make a meal out of your leg. You grab the rusty chef's knife and ...
      
Prepare to fight, because one of you two is on the menu for supper tonight.
And I don't think that you want it to be you that's on the menu tonight / today, you know you can't tell what time of day it is here while trapped in this area as there are no windows or any indicators as to whether it is day or night outside of this place.\n""" + text_end)

input("Just before the giant rat can attack you. A feeling washes over you and you are transported to your inner soul space where time from the outside world seems to have slowed to a stop.\n\nThe Guiding Force whispers in your mind 'Remember to just breathe.' When you have collected your thoughs,\nPress " + text_invert + "'Enter'" + text_end + " to continue:\n\n")

print("One more thing ...\n")
time.sleep(2)
print("The only way out is forward.\nYou can go forward.\nYou can go left.\nYou can go right.\n\n")
time.sleep(5)
print("But you can never.\n\n")
time.sleep(2)
print("And I mean NEVER go back the way you came!\n\n")
nod_in_agreement = input("Let that sink into your little noodle.\nYou can nod your head in agreement by pressing " + text_invert + "'Enter'" + text_end + " to continue:")
time.sleep(2)
print("\n\nTake a breath, don't stress and remember ...\n")
time.sleep(2)
print("...\n\n")
time.sleep(2)
print("Do not say that ...\n")
time.sleep(2)
print("Yooouuuuu ...\n")
time.sleep(2)
print("Have ...\n")
time.sleep(2)
print("NOT ...\n")
time.sleep(2)
print("BEEN ...\n")
time.sleep(2)
print(text_color_red + "WARNED!!!\n" + text_end)
time.sleep(2)
print("\n\n")

# Starting basic player stats.
player_stats = {"name": "Soandso", "gender": "Gender Nil", "race": "Human", "strength": 10, "dexterity": 10, "constitution": 10, "level": 1, "experience": 0, "alive": True}



player_name = input("What is your name, brave soul?\nIf you don't answer, I will pick one for you:   ")
if len(player_name) == 0:
    print("\nYour name shall be set as 'Soandso'\nLet's move on the next question.")        
else:
    player_stats.update({"name": player_name})
    print(f"\n\nHello {player_name}.")

player_gender = input("\n\nWhat gender do you identify as?\n\nIf you don't pick one, I'll set you as 'Gender Nil':   ")
if len(player_gender) == 0:
    print("\nYour gender shall be set as 'Gender Nil'\nMoving on from the questions.\n")
else:
    player_stats.update({"gender": player_gender})
    print(f"Well, you seem to resemble a {player_gender}.\n\nAnyways, moving on.")

print(f"Now, {player_name}, all of your base stats start off as 10 each. You have 10 points to add to your stats. The stats that you are concerned with are as follows:")
print("\nStrength: This determines how hard you can hit and how easily you hit with melee weapons.")
move_on = input("Press " + text_invert + "'Enter'" + text_end + " to continue:")
print("\nDexterity: This determines how well you can avoid attacks while also determining how well you can hit with ranged weapons.")
move_on = input("Press " + text_invert + "'Enter'" + text_end + " to continue:")
print("\nConstitution: This determines how healthy you are and how well you can shrug off the effects of diseases, illnesses, and poisons.")
move_on = input("Press " + text_invert + "'Enter'" + text_end + " to continue:")

player_remaining_stat_points = 10
player_stat_points_added = 0
player_stat_choice = ""
stat_update = 0

print("\nWhich one of the stats would you like to add points to first?\n")
print("1. Strength, 2. Dexterity, or 3. Constitution\nThese all start with a base of 10 which gives you a +0 to your modifiers. You gain +1 to your modifiers every 2 points over 10 that you allocate to your stats.\n\nMake your choices.\n")
print(f"Your current stats are as follows:\nStrength: {player_stats['strength']}\nDexterity: {player_stats['dexterity']}\nConstitution: {player_stats['constitution']}\n")

time.sleep(3)

while player_remaining_stat_points > 0:
    print(f"You have {player_remaining_stat_points} stat points remaining to be distributed.\nPlease select from the following choices:\n")
    time.sleep(2)
    player_stat_choice = input("1. Strength, 2. Dexterity, or 3. Constitution\n")
    player_stat_choice = int(player_stat_choice)
    if player_stat_choice == 1:
        player_stat_points_added = input(f"How many points of your remaining {player_remaining_stat_points} would you like to add to your Strength?\n:")
        player_stat_points_added = int(player_stat_points_added)
        if player_stat_points_added == 0:
            print("\nYou have opted to add 0 points to Strength.\nChange your mind did we?\n\nMake another selection.")
        elif player_stat_points_added > player_remaining_stat_points:
            print(f"\nYou have selected more points than what you have available.\nPlease select a number of points to add to your 'Strength' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
        else:
            stat_update = player_stats["strength"] + player_stat_points_added
            print(f"You have opted to add {player_stat_points_added} to your current strength score of {player_stats['strength']}. This will make your new Strength score {stat_update}.\n")
            player_stats.update({"strength": stat_update})
            player_remaining_stat_points -= player_stat_points_added

    elif player_stat_choice == 2:
        player_stat_points_added = input(f"How many points of your remaining {player_remaining_stat_points} would you like to add to your Dexterity?\n:")
        player_stat_points_added = int(player_stat_points_added)
        if player_stat_points_added == 0:
            print("\nYou have opted to add 0 points to Dexterity.\nChange your mind did we?\n\nMake another selection.")
        elif player_stat_points_added > player_remaining_stat_points:
            print(f"\nYou have selected more points than what you have available.\nPlease select a number of points to add to your 'Dexterity' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
        else:
            stat_update = player_stats["dexterity"] + player_stat_points_added
            print(f"You have opted to add {player_stat_points_added} to your current Dexterity score of {player_stats['dexterity']}. This will make your new Dexterity score {stat_update}.\n")
            player_stats.update({"dexterity": stat_update})
            player_remaining_stat_points -= player_stat_points_added

    elif player_stat_choice == 3:
        player_stat_points_added = input(f"How many points of your remaining {player_remaining_stat_points} would you like to add to your Constitution?\n:")
        player_stat_points_added = int(player_stat_points_added)
        if player_stat_points_added == 0:
            print("\nYou have opted to add 0 point to Constitution.\nChange your mind did we?\n\nMake another selection.")
        elif player_stat_points_added > player_remaining_stat_points:
            print(f"\nYou have selected more points than what you have available.\nPlease select a number of points to add to your 'Constitution' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
        else:
            stat_update = player_stats["constitution"] + player_stat_points_added
            print(f"You have opted to add {player_stat_points_added} to your current Constitution score of {player_stats['constitution']}. This will make your new Constitution score {stat_update}.\n")
            player_stats.update({"constitution": stat_update})
            player_remaining_stat_points -= player_stat_points_added
    else:
        print("\nYou did not select Strength, Dexterity, or Constitution.")
        print("Please choose one of the stats above.\n")



# Testing an alternative was of establishing a player. If this works then I can expand a different dictionary to create multiple types of monsters with the same class instead of having to create a new class for every monster type.

class Player:
    def __init__(self, player_stats):
        for key, value in player_stats.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return f'PlayerCharacter("All you know is that you are a {self.gender} {self.race} and you think that your name is "{self.name}"\nYou think that is your name at least.'

player_equipment = {"weapon": "Rusty Kitchen Knife", "armor": "rags", "gold": 0}

test_player = Player(player_stats)
# This section is just for testing to make sure that the fields are being properly set.
print(f"Player's Name: {test_player.name}")
print(f"Player's Gender: {test_player.gender}")
print(f"Player's Race: {test_player.race}")
print(f"Player's Strength: {test_player.strength}")
print(f"Player's Dexterity: {test_player.dexterity}")
print(f"Player's Constitution: {test_player.constitution}")
print(f"Player's Level: {test_player.level}")
print(f"Player's Experience: {test_player.experience}")
print(f"Player's Living Status: {test_player.alive}")

'''
    
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
mob = dict_kobold

bob = Monster(mob)

#This is just to test is the monsters are pulling all of the right info from the dictionary
print("\n\nThis is the monster's stats\n\n")
print(f"Monster's Name: {(bob.name)}")
print(f"Monster's Hit Points: {bob.hit_points}")
print(f"Monster's To Hit Modifier: {bob.to_hit}")
print(f"Monster's Damage: {bob.damage}")
print(f"Monster's Defence Rating: {bob.defense_rating}")
print(f"Monster's Experience: {bob.experience_value}")
print(f"Monster's Gold: {bob.gold}")
print(f"Monster's Living Status: {bob.is_alive}")

# Main code below here.

# Random Dice Rollers

#to_hit_dice = random.randint(1, 20)
#damage_dice = random.randint(1, 8)
# Testing random number generator
#for i in range(0, 10):
    #damage_dice = random.randint(1, 8)
    #
    # print(f"Random damage die rolls: {damage_dice} + 1 = " + str((damage_dice + 1)))


goodbye = input("Press " + text_invert + "'Enter'" + text_end + " to exit.")
os.system('cls' if os.name == 'nt' else 'clear')