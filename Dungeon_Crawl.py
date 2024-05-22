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


# These are the initializing variables.
strength_bonus = 0
dexterity_bonus = 0
constitution_bonus = 0
player_attack_bonus = 1
player_defense = 10
hit_points = 10
player_remaining_stat_points = 10
player_stat_points_added = 0
player_stat_choice = ""
stat_update = 0


# These are the dictionaries, lists, and variables of weapons, armor, potions, monsters, etc...

# Starting basic player stats.
dict_player_stats = {"name": "Soandso", "gender": "Genderless", "race": "Human", "strength": 10, "strength_bonus": strength_bonus, "dexterity": 10, "dexterity_bonus": dexterity_bonus, "constitution": 10, "constitution_bonus": constitution_bonus, "player_defense_rating": player_defense, "player_attack_bonus": player_attack_bonus, "level": 1, "experience": 0, "hit_points": hit_points, "is_alive": True}

# Stats and their bonuses
dict_stat_bonues = {2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10}

# Player Attack Bonus "Level": "player_attack_bonus"
dict_player_attack_bonus = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5}

# Players Menu
dict_menu_list = {"w": "Move forward", "a": "Go left", "s": "Turn back", "d": "Go right", "c": "Character sheet", "i": "Inventory", "q": "Quaff a Potion", "l": "Look Around"}

# Player Monster Encounter 
dict_mob_menu = {"a": "Attack - Melee", "b": "Attack - Ranged", "f": "Flee"}

# "Weapon name": [Number of Damage, Value of Damage Damage, Cost, type of attack "melee" or "ranged"]
dict_weapons_melee = {"rusty kitchen knife": (1, 4, 1, "melee"), "shortsword": [1, 6, 10, "melee"], "longsword": [1, 8, 20, "melee"], "greatsword": [2, 6, 50, "melee"]}

# "Weapon name": Number of Damage, Value of Damage Damage, Cost, type of attack "melee" or "ranged"
dict_weapons_ranged = {"throwing knife": [1, 3, 1, "ranged"], "shortbow": [1, 6, 10, "ranged"], "songbow": [1, 8, 20, "ranged"], "heavy crossbow": [2, 6, 50, "ranged"]}

# "Bonus Damage: -5 through +5"
dict_damage_modifier = {"Crippling": -5, "Debilitating": -4, "Weakening": -3, "Hampering": -2, "Slight Impairment": -1, "Normal": 0, "Slight Enhancement": 1, "Boosting": 2, "Strengthening": 3, "Empowering": 4, "Potent": 5}

# "Armor name": [Defence value, cost]
dict_armors = {"rags": [1, 0], "cloth armor": [2, 10], "leather armor": [3, 25], "chainmail": [6, 70], "platemail": [ 8, 200]}

# "Healing potion name": [Healing value, cost].
dict_potions = {"potion of healing": [30, 15], "elixir of healing": [60, 40], "infustion of healing": [120, 100], "tincture of healing": [300, 250]}

# {0 - name: xyz, 1 - hit_points = 5, 2 - to_hit = 1, 3 - damage = 3, 4 - defence_rating = 4, 5 - experience_value = 7, 6 - gold = 3, 7 - is_alive = True}
dict_monsters = {1: 'dict_giant_rat', 2: 'dict_goblin', 3: 'dict_kobold'}

dict_giant_rat = {"name": "giant rat", "hit_points": 7, "to_hit": 4, "damage": [1, 2], "defense_rating": 11, "experience_value": 25, "gold": 3, "is_alive": True} 
dict_goblin = {"name": "goblin", "hit_points": 7, "to_hit": 4, "damage": [1, 5], "defense_rating": 13, "experience_value": 10, "gold": 5, "is_alive": True} 
dict_kobold = {"name": "kobold", "hit_points": 5, "to_hit": 4, "damage": [1, 3], "defense_rating": 12, "experience_value": 25, "gold": 7, "is_alive": True}

#This is assigning the starting name, gender, and attribute points. 
def character_creation():
    player_name = input("What is your name, brave soul?\nIf you don't answer, I will pick one for you:   ")
    if len(player_name) == 0:
        print("\nYour name shall be set as 'Soandso'\nLet's move on the next question.")        
    else:
        dict_player_stats.update({"name": player_name})
        print(f"\n\nHello {player_name}.")
        player_gender = input("\n\nWhat gender do you identify as?\n\nIf you don't pick one for you:   ")
    if len(player_gender) == 0:
        print("\nYour gender shall be set as 'Genderless'\nMoving on from the questions.\n")
    else:
        dict_player_stats.update({"gender": player_gender})
        print(f"Well, you seem to resemble a {player_gender}.\n\nAnyways, moving on.")

        print(f"Now, {dict_player_stats["name"]}, all of your base stats start off as 10 each. You have 10 points to add to your stats. The stats that you are concerned with are as follows:")
        print("\nStrength: This determines how hard you can hit and how easily you hit with melee weapons.")
        move_on = input("Press " + text_invert + "'Enter'" + text_end + " to continue:")
        print("\nDexterity: This determines how well you can avoid attacks while also determining how well you can hit with ranged weapons.")
        move_on = input("Press " + text_invert + "'Enter'" + text_end + " to continue:")
        print("\nConstitution: This determines how healthy you are and how well you can shrug off the effects of diseases, illnesses, and poisons.")
        move_on = input("Press " + text_invert + "'Enter'" + text_end + " to continue:")

        print("\nWhich one of the stats would you like to add points to first?\n")
        print("1. Strength, 2. Dexterity, or 3. Constitution\nThese all start with a base of 10 which gives you a +0 to your modifiers. You gain +1 to your modifiers every 2 points over 10 that you allocate to your stats.\n\nMake your choices.\n")
        print(f"Your current stats are as follows:\nStrength: {dict_player_stats['strength']}\nDexterity: {dict_player_stats['dexterity']}\nConstitution: {dict_player_stats['constitution']}\n")

        #time.sleep(3)


# Turn this into a method. Build in way to add stat points with levelups.
def increase_stats(player_remaining_stat_points):
    while player_remaining_stat_points > 0:
        print(f"You have {player_remaining_stat_points} stat points remaining to be distributed.")
        print(f"Your current stats are as follows:\nStrength: {dict_player_stats['strength']}\nDexterity: {dict_player_stats['dexterity']}\nConstitution: {dict_player_stats['constitution']}\n")
        print("Please select from the following choices:\n")
        #time.sleep(2)
        player_stat_choice = input("1. Strength, 2. Dexterity, or 3. Constitution\n")
        if not player_stat_choice:
            print("\nYou did not select Strength, Dexterity, or Constitution.")
            print("Please choose one of the stats above.\n")
            continue
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
                print(f"\n{dict_player_stats['name']}, you have opted to add 0 points to Dexterity.\nChange your mind did we?\n\nMake another selection.")
            elif player_stat_points_added > player_remaining_stat_points:
                print(f"\n{dict_player_stats['name']}, you have selected more points than what you have available.\nPlease select a number of points to add to your 'Dexterity' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
            else:
                stat_update = dict_player_stats["dexterity"] + player_stat_points_added
                print(f"{dict_player_stats['name']}, you have opted to add {player_stat_points_added} to your current Dexterity score of {dict_player_stats['dexterity']}. This will make your new Dexterity score {stat_update}.\n")
                dict_player_stats.update({"dexterity": stat_update})
                player_remaining_stat_points -= player_stat_points_added

        elif player_stat_choice == 3:
            player_stat_points_added = input(f"How many points of your remaining {player_remaining_stat_points} would you like to add to your Constitution?\n:")
            player_stat_points_added = int(player_stat_points_added)
            if player_stat_points_added == 0:
                print(f"\n{dict_player_stats['name']}, you have opted to add 0 point to Constitution.\nChange your mind did we?\n\nMake another selection.")
            elif player_stat_points_added > player_remaining_stat_points:
                print(f"\n{dict_player_stats['name']}, you have selected more points than what you have available.\nPlease select a number of points to add to your 'Constitution' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
            else:
                stat_update = dict_player_stats["constitution"] + player_stat_points_added
                print(f"{dict_player_stats['name']}, you have opted to add {player_stat_points_added} to your current Constitution score of {dict_player_stats['constitution']}. This will make your new Constitution score {stat_update}.\n")
                dict_player_stats.update({"constitution": stat_update})
                player_remaining_stat_points -= player_stat_points_added
        else:
            print(f"\n{dict_player_stats['name']}, you did not select Strength, Dexterity, or Constitution.")
            print("Please choose one of the stats above.\n")

# This is to update the stats and ability modifiers after every time the player gains stat points.
def update_stats_and_bonuses():
    player_score_strength = dict_player_stats["strength"]
    strength_bonus = dict_stat_bonues[player_score_strength]
    dict_player_stats.update({"strength_bonus": strength_bonus})

    player_score_dexterity = dict_player_stats["dexterity"]
    dexterity_bonus = dict_stat_bonues[player_score_dexterity]
    dict_player_stats.update({"dexterity_bonus": dexterity_bonus})

    player_score_constitution = dict_player_stats["constitution"]
    constitution_bonus = dict_stat_bonues[player_score_constitution]
    dict_player_stats.update({"constitution_bonus": constitution_bonus})
    updated_hitpoints = hit_points + constitution_bonus
    dict_player_stats.update({"hit_points": updated_hitpoints})

# Dice Roller Function
def Roll_Dice(dice_number, dice_type, silent = False):
    dice_roll_total = 0
    die_number = 1
    if dice_number == 1:
        die_roll = random.randint(1, dice_type)
        if not silent:
             print(f"Rolling '{dice_number}d{dice_type}'.")
             print(f"The die roll is: {die_roll}")
             dice_roll_total += die_roll
        else:
             dice_roll_total += die_roll

    else:
        die_number = 1
        for _ in range(dice_number):
            die_roll = random.randint(1, dice_type)
            if not silent:
                 print(f"Rolling '{dice_number}d{dice_type}'.")
                 print(f"Die number {die_number}'s roll is: {die_roll}")
                 die_number += 1
                 dice_roll_total += die_roll
            else:
                 die_number += 1
                 dice_roll_total += die_roll
    if not silent:
        print(f"The roll total was {dice_roll_total}")
    return dice_roll_total

# Establishing the class object for the player.
class Player:

    # Instantiate the player character, starting stats, and starting equipment.
    def __init__(self, dict_player_stats):
        for key, value in dict_player_stats.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return f'PlayerCharacter("All you know is that you are a {self.race} {self.gender} and you think that your name is \'{self.name}\'\nAt least you think that it is.")'
    
    # Display the players currently held inventory
    def check_inventory(self):
        print("You have the following items in your inventory")
        for key, value in player_equipment.items():
            print(f"{key}: {value}")

    # Display the list of options a player can do.
    def player_menu(self):
        print("Select from the options below:")
        for key, value in dict_menu_list.items():
            print(f"{key}: {value}", end="  ")
    
    # Attack Code using the standard D20 system. Roll 1d20 + attack bonus + attack stat bonus >= Defenders Defence/AC rating.

    def attack(self, attack_type):
        self.attack_type = attack_type
        if attack_type == "melee":
            if player_equipment["weapon_melee"] == "none":
                print("You are not currently holding a melee weapon")
                to_hit_monster = 0
            else:
                print(f"You attack a {enemy.name} with your {player_equipment["weapon_melee"]}")
                die_roll = Roll_Dice(1, 20)
                attack_bonus = player_character.player_attack_bonus + player_character.strength_bonus
                print(f"\nPlayer Attack Bonus = {player_character.player_attack_bonus}\n\nPlayer Strength Bonus = {player_character.strength_bonus}")
                to_hit_monster = die_roll + attack_bonus
                print(f"Total Attack Roll: {to_hit_monster}")
        else:
            if player_equipment["weapon_ranged"] == "none":
                print("You are not currently holding a ranged weapon.")
                to_hit_monster = 0
            else:
                print(f"You attack a {enemy.name} with your {player_equipment["weapon_ranged"]}")
                die_roll = Roll_Dice(1, 20)
                attack_bonus = player_character.player_attack_bonus + player_character.dexterity_bonus
                to_hit_monster = die_roll + attack_bonus
                print(f"Total Attack Roll: {to_hit_monster}")
        return to_hit_monster


player_equipment = {"weapon_melee": "rusty kitchen knife","weapon_ranged": "none", "armor": "rags", "gold": 0, "items": ["a small pebble", "rope belt", "a flagon of ale"]}
player_armor_defence = player_equipment["armor"]
player_defense = 10 + dict_player_stats["dexterity_bonus"] + dict_armors[player_armor_defence][0]
dict_player_stats.update({"player_defense_rating": player_defense})
player_character = Player(dict_player_stats)

# This section is just for testing to make sure that the fields are being properly set.
'''print("Testing the menu display options")
player_character.player_menu()
print(" ")
print("Testing the check inventory function.")
player_character.check_inventory()'''

'''

    def move():
        pass

    def open():
        pass
'''
# Random monster generator. This is to randomly select one of the mobs in the dict_monsters dictionary.

def Random_Monster():
    mob = dict_monsters[Roll_Dice(1, len(dict_monsters), True)]
    mob = globals()[mob]
    return mob
    


class Monster:
    def __init__(self, mob):
        for key, value in mob.items():
            setattr(self, key, value)
    
    def attack(self):
        print(f"A {enemy.name} viciously attacks you.")
        die_roll = Roll_Dice(1, 20, False)
        to_hit_player = die_roll + enemy.to_hit
        print(f"Enemy's To Hit = {enemy.to_hit}")
        return to_hit_player

# Test mobs


mob = Random_Monster()
enemy = Monster(mob)

# FIGHT CLUB! reference dictionaries below.
# Monster Dict {0 - name: goblin, 1 - hit_points = 5, 2 - to_hit = 1, 3 - damage = 3, 4 - defence_rating = 4, 5 - experience_value = 7, 6 - gold = 3, 7 - is_alive = True}
# Player Dict {"name": "Soandso", "gender": "Gender Nil", "race": "Human", "strength": 10, "strength_bonus": strength_bonus, "dexterity": 10, "dexterity_bonus": dexterity_bonus, "constitution": 10, "constitution_bonus": constitution_bonus, "player_attack_bonus": player_attack_bonus, "level": 1, "experience": 0, "alive": True}
# Equipment Dict"weapon_melee": "rusty kitchen knife","weapon_ranged": "none", "armor": "rags", "gold": 0, "items": ["a small pebble", "rope belt", "a flagon of ale"]}
# Weapons Dict 0 - "Weapon name": [Number of dice to roll, type of dice to roll, Cost of the weapon, type of attack "melee" or "ranged"]
def fight_club(attacker, attack_type = "none"):
    to_hit_monster = 0
    hit_player = 0
    if attacker == player_character:
        if player_character.is_alive is True:
            if attack_type == "melee":
                equiped_weapon = player_equipment["weapon_melee"]
                ability_modifier = player_character.strength_bonus
            elif attack_type == "ranged":
                equiped_weapon = player_equipment["weapon_ranged"]
                ability_modifier = player_character.dexterity_bonus
            else:
                print("You are not equiped with a melee or ranged weapon.")
            
            print(f"You are attacking a {enemy.name}")
            to_hit_monster = player_character.attack(attack_type)
            if to_hit_monster >= enemy.defense_rating:
                number_of_dice = dict_weapons_melee[equiped_weapon][0]
                type_of_dice = dict_weapons_melee[equiped_weapon][1]
                damage_to_monster = Roll_Dice(number_of_dice, type_of_dice) + ability_modifier
                print(f"You successfully hit a {enemy.name} for {damage_to_monster} points of damage.")
                enemy.hit_points -= damage_to_monster
                if enemy.hit_points <= 0:
                    enemy.is_alive = False
                    print(f"You have successfully defeated a {enemy.name}.")
                    print(f"You have gained {enemy.experience_value} points of experience.")
                    player_character.experience += enemy.experience_value
                    print(f"{dict_player_stats['name']}, you now have a total of {player_character.experience} points of experience.")
            else:
                print(f"You missed a {enemy.name}.")
        else:
            print("You can't attack, you're dead.\n\nBetter luck next time.")
    else:
        if enemy.is_alive is True:
            attacker = enemy.name
            print(f"A {enemy.name} attacks you:")
            hit_player = enemy.attack()
            if hit_player >= player_character.player_defense_rating:
                number_of_dice = enemy.damage[0]
                type_of_dice =  enemy.damage[1]
                damage_to_player = Roll_Dice(number_of_dice, type_of_dice, True)
                print(f"A {enemy.name} has hit you for {damage_to_player} points of damage.")
                player_character.hit_points -= damage_to_player
                if player_character.hit_points <= 0:
                    player_character.is_alive = False
                    print(f"You have succumbed to your wounds inflicted by a {enemy.name}")
            else:
                print(f"A {enemy.name} has missed you.")
        else:
            print("The enemy is dead. There's no use in beating a dead horse to death.")

# List current stats and inventory.
#dict_player_stats = {"name", "gender": "Gender Nil", "race": "Human", "strength": 10, "strength_bonus": strength_bonus, "dexterity": 10, "dexterity_bonus": dexterity_bonus, "constitution": 10, "constitution_bonus": constitution_bonus, "player_defense_rating": player_defense, "player_attack_bonus": player_attack_bonus, "level": 1, "experience": 0, "hit_points": hit_points, "is_alive": True}
def current_stats_and_inventory():
    print(f"Your current stats are as follows:\nStrength:\t{dict_player_stats['strength']}\nDexterity:\t{dict_player_stats['dexterity']}\nConstitution:\t{dict_player_stats['constitution']}\n")
    player_character.check_inventory()


# Main code below here.
##### Main #####

# The story thus far ...
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
#time.sleep(2)
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



'''while player_character.is_alive is True  and enemy.is_alive is True:
    fight_club(player_character, "melee")
    print(f"\n\n{enemy.name} has {enemy.hit_points} health remaining.\n\n")
    print("The Enemy's Turn!!!!\n\n")
    fight_club(enemy)
    print(f"\n\nYou have {player_character.hit_points} health remaining.\n\n")
    continue_on = input("Press " + text_invert + "'Enter'" + text_end + " to Continue.")
'''
character_creation()

increase_stats(player_remaining_stat_points)
update_stats_and_bonuses()
current_stats_and_inventory()

print("This is where the adventure begins.")



goodbye = input("Press " + text_invert + "'Enter'" + text_end + " to exit.")
os.system('cls' if os.name == 'nt' else 'clear')