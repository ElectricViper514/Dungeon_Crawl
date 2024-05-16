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

from email import message_from_file
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
print("The only way out is forward.\n\nYou can go forward.\nYou can go left.\nYou can go right.\nHeck, you can even go turn around and go back the way you came.\n\n")
#time.sleep(5)
print(text_color_red + "But you should never.\n\n")
#time.sleep(2)
print("And I mean " + text_invert + "NEVER" + text_end + text_color_red + " go back the way you came!\nYou never know if a Grue might eat you alive.\n\n" + text_end)
#time.sleep(3)
nod_in_agreement = input("Let that sink into your pretty little noggin for a moment.\n\nYou can nod your pretty little head in agreement once your new reality has sunken in by: \npressing " + text_color_green + text_invert + "'Enter'" + text_end + " to continue:\n")
#time.sleep(2)
print("\n\nTake a breath, don't stress, and remember ...\n")
#time.sleep(2)
print("...\n\n")
#time.sleep(2)
print("Do not say that ...\n")
#time.sleep(2)
print("Yooouuuuu ...\n")
#time.sleep(2)
print("Were ...\n")
#time.sleep(2)
print("NOT ...\n")
#time.sleep(2)
print(text_color_red + "WARNED!!!\n" + text_end)
#time.sleep(2)
print("\n\n")

# These are the initializing variables.
strength_bonus = 0
dexterity_bonus = 0
constitution_bonus = 0
player_attack_bonus = 1

# These are the dictionaries, lists, and variables of weapons, armor, potions, monsters, etc...

# Starting basic player stats.
dict_player_stats = {"name": "Soandso", "gender": "Gender Nil", "race": "Human", "strength": 10, "strength_bonus": strength_bonus, "dexterity": 10, "dexterity_bonus": dexterity_bonus, "constitution": 10, "constitution_bonus": constitution_bonus, "attack_bonus": player_attack_bonus, "level": 1, "experience": 0, "alive": True}

# Stats and their bonuses
dict_stat_bonues = {2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10}

# Player Attack Bonus "Level": "attack_bonus"
dict_player_attack_bonus = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5}

# Players Menu
dict_menu_list = {"w": "Move forward", "a": "Go left", "s": "Turn back", "d": "Go right", "c": "Character sheet", "i": "Inventory", "q": "Quaff a Potion", "l": "Look Around"}

# Player Monster Encounter 
dict_mob_menu = {"a": "Attack - Melee", "b": "Attack - Ranged", "f": "Flee"}

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


player_name = input("What is your name, brave soul?\nIf you don't answer, I will pick one for you:   ")
if len(player_name) == 0:
    print("\nYour name shall be set as 'Soandso'\nLet's move on the next question.")        
else:
    dict_player_stats.update({"name": player_name})
    print(f"\n\nHello {player_name}.")

player_gender = input("\n\nWhat gender do you identify as?\n\nIf you don't pick one, I'll set you as 'Gender Nil':   ")
if len(player_gender) == 0:
    print("\nYour gender shall be set as 'Gender Nil'\nMoving on from the questions.\n")
else:
    dict_player_stats.update({"gender": player_gender})
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
print(f"Your current stats are as follows:\nStrength: {dict_player_stats['strength']}\nDexterity: {dict_player_stats['dexterity']}\nConstitution: {dict_player_stats['constitution']}\n")

#time.sleep(3)

# Turn this into a method. Build in way to add stat points with levelups.
while player_remaining_stat_points > 0:
    print(f"You have {player_remaining_stat_points} stat points remaining to be distributed.\nPlease select from the following choices:\n")
    #time.sleep(2)
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
            stat_update = dict_player_stats["strength"] + player_stat_points_added
            print(f"You have opted to add {player_stat_points_added} to your current strength score of {dict_player_stats['strength']}. This will make your new Strength score {stat_update}.\n")
            dict_player_stats.update({"strength": stat_update})
            player_remaining_stat_points -= player_stat_points_added

    elif player_stat_choice == 2:
        player_stat_points_added = input(f"How many points of your remaining {player_remaining_stat_points} would you like to add to your Dexterity?\n:")
        player_stat_points_added = int(player_stat_points_added)
        if player_stat_points_added == 0:
            print("\nYou have opted to add 0 points to Dexterity.\nChange your mind did we?\n\nMake another selection.")
        elif player_stat_points_added > player_remaining_stat_points:
            print(f"\nYou have selected more points than what you have available.\nPlease select a number of points to add to your 'Dexterity' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
        else:
            stat_update = dict_player_stats["dexterity"] + player_stat_points_added
            print(f"You have opted to add {player_stat_points_added} to your current Dexterity score of {dict_player_stats['dexterity']}. This will make your new Dexterity score {stat_update}.\n")
            dict_player_stats.update({"dexterity": stat_update})
            player_remaining_stat_points -= player_stat_points_added

    elif player_stat_choice == 3:
        player_stat_points_added = input(f"How many points of your remaining {player_remaining_stat_points} would you like to add to your Constitution?\n:")
        player_stat_points_added = int(player_stat_points_added)
        if player_stat_points_added == 0:
            print("\nYou have opted to add 0 point to Constitution.\nChange your mind did we?\n\nMake another selection.")
        elif player_stat_points_added > player_remaining_stat_points:
            print(f"\nYou have selected more points than what you have available.\nPlease select a number of points to add to your 'Constitution' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
        else:
            stat_update = dict_player_stats["constitution"] + player_stat_points_added
            print(f"You have opted to add {player_stat_points_added} to your current Constitution score of {dict_player_stats['constitution']}. This will make your new Constitution score {stat_update}.\n")
            dict_player_stats.update({"constitution": stat_update})
            player_remaining_stat_points -= player_stat_points_added
    else:
        print("\nYou did not select Strength, Dexterity, or Constitution.")
        print("Please choose one of the stats above.\n")

# Set this up to update after every time the player gains stat points.
player_score_strength = dict_player_stats["strength"]
strength_bonus = dict_stat_bonues[player_score_strength]
dict_player_stats.update({"strength_bonus": strength_bonus})

player_score_dexterity = dict_player_stats["dexterity"]
dexterity_bonus = dict_stat_bonues[player_score_dexterity]
dict_player_stats.update({"dexterity_bonus": dexterity_bonus})

player_score_constitution = dict_player_stats["constitution"]
constitution_bonus = dict_stat_bonues[player_score_constitution]
dict_player_stats.update({"constitution_bonus": constitution_bonus})



# Dice Roller Function
def Roll_Dice(dice_number, dice_type, silent = False):
    dice_roll_total = 0
    die_number = 1
    print(f"You are rolling '{dice_number}d{dice_type}'.")
    
    if dice_number == 1:
        die_roll = random.randint(1, dice_type)
        if not silent:
             print(f"Your die roll is: {die_roll}")
             dice_roll_total += die_roll
        else:
             dice_roll_total += die_roll

    else:
        die_number = 1
        for _ in range(dice_number):
            die_roll = random.randint(1, dice_type)
            if not silent:
                 print(f"Die number {die_number}'s roll is: {die_roll}")
                 die_number += 1
                 dice_roll_total += die_roll
            else:
                 die_number += 1
                 dice_roll_total += die_roll
    
    print(f"Your roll total was {dice_roll_total}")

# Establishing the class object for the player.
class Player:

    def __init__(self, dict_player_stats):
        for key, value in dict_player_stats.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return f'PlayerCharacter("All you know is that you are a {self.race} {self.gender} and you think that your name is \'{self.name}\'\nAt least you think that it is.")'
    
    def check_inventory(self):
        print("You have the following items in your inventory")
        for key, value in player_equipment.items():
            print(f"{key}: {value}")

    def player_menu(self):
        print("Select from the options below:")
        for key, value in dict_menu_list.items():
            print(f"{key}: {value}", end="  ")
    
    # Attack Code roll 1d20 + attack bonus + attack stat bonus >= Defenders Defence/AC rating.
    def attack(attack_type):
        if attack_type == "melee":
            die_roll = Roll_Dice(1, 20)
            attack_bonus = player_character.player_attack_bonus + player_character.strength_bonus
            to_hit = die_roll + attack_bonus
        
        else:
            die_roll = Roll_Dice(1, 20)
            attack_bonus = player_character.player_attack_bonus + player_character.dexterity_bonus
            to_hit = die_roll + attack_bonus
        
        return to_hit


player_equipment = {"weapon": "Rusty Kitchen Knife", "armor": "rags", "gold": 0, "items": ["a small pebble", "rope belt", "a flagon of ale"]}

player_character = Player(dict_player_stats)
# This section is just for testing to make sure that the fields are being properly set.
print("Testing the menu display options")
player_character.player_menu()
print(" ")
print("Testing the check inventory function.")
player_character.check_inventory()


print(f"Player's Strength is: {player_character.strength}")
print(player_character.strength_bonus)
'''
    
    def attack(self, attack_rating, damage):
        self.attack_rating = attack_rating
        self.damage = damage

    def quaff_potion():
        pass

    def move():
        pass

    def open():
        pass
'''
class Monster:
    def __init__(self, mob):
        for key, value in mob.items():
            setattr(self, key, value)

# Create random monster generator
mob = {}
mob = dict_giant_rat

bob = Monster(mob)

print("\n\nPC melee attack:")        
player_character.attack('melee')
print("\n\nPC ranged attack:")
player_character.attack("ranged")

# Main code below here.




goodbye = input("Press " + text_invert + "'Enter'" + text_end + " to exit.")
os.system('cls' if os.name == 'nt' else 'clear')