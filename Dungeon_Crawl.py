#!/usr/bin/env python
# https://github.com/ElectricViper514/Dungeon_Crawl

'''This is my first portfolio project from Codecademy. I am going to create a very simple text based
dungeon crawl where the player will be able to select their name. They will start with a small back
story and then they will be able to explore, encounter enemies, fight, flee, heal, and shop. There
will be a simple inventory management system.
A more detailed outline can be found within README.py'''

__author__      = "John W. Davis"
__copyright__   = "2024 - The Codecademy Project"
__credits__     = ["John W. Davis"]
__license__     = ""
__version__     = "0.0.1"
__maintainer__  = "John W. Davis"
__website__     = "www.VipersByteSolutions.com"
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
update_strength = 0
update_dexterity = 0
update_constitution = 0
continue_to_next_section = ""
dict_level_experience = {}
level = 1
level_max = 31 #Non inclusive always add 1 to the max level that you are wanting so that it will iterate through the proper levels and exp values in the dictionary.
xp_to_level = 0
monster_in_room = False
player_choice = ""



# These are the dictionaries, lists, and variables of weapons, armor, potions, monsters, etc...

# Starting basic player stats.
dict_player_stats = {"name": "Soandso", "gender": "Genderless", "race": "Human", "strength": 10, "strength_bonus": strength_bonus, "dexterity": 10, "dexterity_bonus": dexterity_bonus, "constitution": 10, "constitution_bonus": constitution_bonus, "player_defense_rating": player_defense, "player_attack_bonus": player_attack_bonus, "level": 1, "experience": 0, "hit_points": hit_points, "is_alive": True}

# Stats and their bonuses
dict_stat_bonues = {2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10}

# Player Attack Bonus "Level": "player_attack_bonus"
dict_player_attack_bonus = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5}

# Player Level 
dict_level_experience = {1: 200, 2: 443, 3: 706, 4: 983, 5: 1270, 6: 1566, 7: 1870, 8: 2180, 9: 2497, 10: 2818, 11: 3145, 12: 3476, 13: 3811, 14: 4150, 15: 4493, 16: 4839, 17: 5188, 18: 5541, 19: 5896, 20: 6254, 21: 6615, 22: 6979, 23: 7345, 24: 7713, 25: 8084, 26: 8457, 27: 8832, 28: 9209, 29: 9589, 30: 9970}

# I am currently using a sliding scale of 1.15. I useed the script below to calculate how much EXP would be needed to progress from one level to the next level.
'''
while level < (level_max):
    xp_to_level = (100 * level) ** 1.15
    exp = round(xp_to_level)
    #print(f"Level {level}: XP needed to the next level is '{exp}'.")
    dict_level_experience[level] = exp
    level += 1 

for key, value in dict_level_experience.items():
    print(f"{key}: {value}")

# time.sleep(5)

'''
# Player's Equipment List
dict_player_equipment = {"weapon_melee": "rusty kitchen knife","weapon_ranged": "none", "armor": "rags", "gold": 0, "items": ["a small pebble", "rope belt", "a flagon of ale", {"Healing Draught": 3}]}

# Players Menu
dict_menu_main = {"W": "Move forward", "A": "Go left", "S": "Turn back", "D": "Go right", "C": "Character sheet", "I": "Inventory", "Q": "Quaff a Potion", "L": "Look Around"}

# Player Monster Encounter 
dict_menu_fight = {"A": "Melee - Attack", "D": "Ranged - Attack", "Q": "Quaff Potion", "F": "Flee"}

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

dict_giant_rat = {"name": "giant rat", "hit_points": 7, "to_hit": 4, "damage": [1, 2], "defense_rating": 11, "experience_value": 5, "gold": 3, "is_alive": True} 
dict_goblin = {"name": "goblin", "hit_points": 7, "to_hit": 4, "damage": [1, 5], "defense_rating": 13, "experience_value": 20, "gold": 5, "is_alive": True} 
dict_kobold = {"name": "kobold", "hit_points": 5, "to_hit": 4, "damage": [1, 3], "defense_rating": 12, "experience_value": 10, "gold": 7, "is_alive": True}

# Room descriptions currently 1 - 10
dict_room_descriptions = {1: "Room 1", 2: "Room 2", 3: "Room 3", 4: "Room 4", 5: "Room 5", 6: "Room 6", 7: "Room 7", 8: "Room 8", 9: "Room 9", 10: "Room 10"}

# Room Exits {1: "Foward", 2: "Right", 3: "Left", 4: "Back"}
dict_room_exits = {1: "Foward", 2: "Right", 3: "Left", 4: "Back"}

#This is assigning the starting name, gender, and attribute points. 
def character_creation():
    player_gender = ""

    player_name = input("What is your name, brave soul?\nIf you don't answer, I will pick one for you:   ")
    if len(player_name) == 0:
        print("\nYour name shall be set as 'Soandso'\nLet's move on the next question.")        
    else:
        dict_player_stats.update({"name": player_name})
        print(f"\n\nHello {player_name}.")
    player_gender = input("\n\nWhat gender do you identify as?\n\nIf you don't pick one, I'll decide for you:   ")
    if len(player_gender) == 0:
        print("\nYour gender shall be set as 'Genderless'\nMoving on from the questions.\n")
    else:
        dict_player_stats.update({"gender": player_gender})
# Test Start
        print("***************Control Print*************")
        print(dict_player_stats["gender"])
        print("************* Test Print ***********")
        player_character.__setattr__("strength", update_strength)
        print(player_character["strength"])
        print("*******************End Test********************")
# End Test


        print(f"\nWell, you seem to resemble a {player_gender}.\n\nAnywho, moving on.\n")

        print("Now, " + text_bold + f"{dict_player_stats["name"]}" + text_end + ", all of your base stats start off as 10 each. You have 10 points to add to your stats. The stats that you are concerned with are as follows:")
        print(text_color_red + "\nStrength: This determines how hard you can hit and how easily you hit with melee weapons.")
        input("Press " + text_invert + "'Enter'" + text_end + text_color_red + " to continue:\n\n" + text_end)
        print(text_color_blue + "\nDexterity: This determines how well you can avoid attacks while also determining how well you can hit with ranged weapons.")
        input("Press " + text_invert + "'Enter'" + text_end + text_color_blue + " to continue:\n\n" + text_end)
        print(text_color_green + "\nConstitution: This determines how healthy you are and how well you can shrug off the effects of diseases, illnesses, and poisons.")
        input("Press " + text_invert + "'Enter'" + text_end + text_color_green + " to continue:\n\n" + text_end)

        print("\nWhich one of the stats would you like to add points to first?\n")
        print(text_color_red + "1. Strength, " + text_end + text_color_blue + "2. Dexterity, " + text_end + "or " + text_color_green + "3. Constitution" + text_end + "\n\nThese all start with a base of 10 which gives you a +0 to your modifiers.\nYou gain +1 to your modifiers every 2 points over 10 that you allocate to your stats.\n\nMake your choices.\n")
        print(f"Your current stats are as follows:\n{text_color_red}Strength: {dict_player_stats['strength']}{text_end}\n{text_color_blue}Dexterity: {dict_player_stats['dexterity']}{text_end}\n{text_color_green}Constitution: {dict_player_stats['constitution']}{text_end}\n")

        # time.sleep(2)


# Turn this into a method. Build in way to add stat points with levelups.
def increase_stats(player_remaining_stat_points):
    while player_remaining_stat_points > 0:
        print(f"You enter your soul space and are greeted by the {text_color_purple}'Guiding Force'{text_end}. She softly whispers into your mind with a distinctly feminine albeit a slightly electrically distorted voice.")
        print(f"You have {player_remaining_stat_points} stat points remaining to be distributed.")
        #print(f"Your current stats are as follows:\nStrength: {dict_player_stats['strength']}\nDexterity: {dict_player_stats['dexterity']}\nConstitution: {dict_player_stats['constitution']}\n")
        print(f"Your current stats are as follows:\n{text_color_red}Strength: {dict_player_stats['strength']}{text_end}\n{text_color_blue}Dexterity: {dict_player_stats['dexterity']}{text_end}\n{text_color_green}Constitution: {dict_player_stats['constitution']}{text_end}\n")
        print(f"Your current stats bonues are as follows:\n{text_color_red}Strength: {dict_player_stats['strength_bonus']}{text_end}\n{text_color_blue}Dexterity: {dict_player_stats['dexterity_bonus']}{text_end}\n{text_color_green}Constitution: {dict_player_stats['constitution_bonus']}{text_end}\n")
        print("Please select from the following choices:\n")
        # time.sleep(1)
        player_stat_choice = input(f"1. {text_color_red}Strength{text_end}, 2. {text_color_blue}Dexterity{text_end}, or 3. {text_color_green}Constitution{text_end}\n")
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
                update_strength = dict_player_stats["strength"] + player_stat_points_added
                print(f"You have opted to add {player_stat_points_added} to your current strength score of {dict_player_stats['strength']}. This will make your new Strength score {update_strength}.\n")
                dict_player_stats.update({"strength": update_strength})
                player_remaining_stat_points -= player_stat_points_added
                # time.sleep(3)
                update_stat_bonuses()

        elif player_stat_choice == 2:
            player_stat_points_added = input(f"How many points of your remaining {player_remaining_stat_points} would you like to add to your Dexterity?\n:")
            player_stat_points_added = int(player_stat_points_added)
            if player_stat_points_added == 0:
                print(f"\n{dict_player_stats['name']}, you have opted to add 0 points to Dexterity.\nChange your mind did we?\n\nMake another selection.")
            elif player_stat_points_added > player_remaining_stat_points:
                print(f"\n{dict_player_stats['name']}, you have selected more points than what you have available.\nPlease select a number of points to add to your 'Dexterity' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
            else:
                update_dexterity = dict_player_stats["dexterity"] + player_stat_points_added
                print(f"{dict_player_stats['name']}, you have opted to add {player_stat_points_added} to your current Dexterity score of {dict_player_stats['dexterity']}. This will make your new Dexterity score {update_dexterity}.\n")
                dict_player_stats.update({"dexterity": update_dexterity})
                player_remaining_stat_points -= player_stat_points_added
                # time.sleep(3)
                update_stat_bonuses()

        elif player_stat_choice == 3:
            player_stat_points_added = input(f"How many points of your remaining {player_remaining_stat_points} would you like to add to your Constitution?\n:")
            player_stat_points_added = int(player_stat_points_added)
            if player_stat_points_added == 0:
                print(f"\n{dict_player_stats['name']}, you have opted to add 0 point to Constitution.\nChange your mind did we?\n\nMake another selection.")
            elif player_stat_points_added > player_remaining_stat_points:
                print(f"\n{dict_player_stats['name']}, you have selected more points than what you have available.\nPlease select a number of points to add to your 'Constitution' that is equal to or lower than your remaining {player_remaining_stat_points} point(s).\n")             
            else:
                update_constitution = dict_player_stats["constitution"] + player_stat_points_added
                print(f"{dict_player_stats['name']}, you have opted to add {player_stat_points_added} to your current Constitution score of {dict_player_stats['constitution']}. This will make your new Constitution score {update_constitution}.\n")
                dict_player_stats.update({"constitution": update_constitution})
                player_remaining_stat_points -= player_stat_points_added
                # time.sleep(3)
                update_stat_bonuses()
        else:
            print(f"\n{dict_player_stats['name']}, you did not select Strength, Dexterity, or Constitution.")
            print("Please choose one of the stats above.\n")
    
    print(f"The {text_color_purple}'Guiding Force'{text_end} smiles at you and fades away appearing as dust in the wind.\nYou blink and the plain white void of a room is once again replaced with the lovely smell of damp, rot, and musty smell of your new reality.\n\n{text_bold}The dungeon.{text_end}")

# This is to update the stats and ability modifiers after every time the player gains stat points.
def update_stat_bonuses():
    print("\n\n\nUpdating stat bonues.\n\n")
    player_score_strength = dict_player_stats["strength"]
    #player_score_strength = player_character["strength"]
    strength_bonus = dict_stat_bonues[player_score_strength]
    dict_player_stats.update({"strength_bonus": strength_bonus})
    print(text_color_red + f"Player Strength Bonus: {dict_player_stats["strength_bonus"]}\n" + text_end)

    player_score_dexterity = dict_player_stats["dexterity"]
    dexterity_bonus = dict_stat_bonues[player_score_dexterity]
    dict_player_stats.update({"dexterity_bonus": dexterity_bonus})
    print(text_color_blue + f"Player Dexterity Bonus: {dict_player_stats["dexterity_bonus"]}\n" + text_end)

    player_score_constitution = dict_player_stats["constitution"]
    constitution_bonus = dict_stat_bonues[player_score_constitution]
    dict_player_stats.update({"constitution_bonus": constitution_bonus})
    updated_hitpoints = hit_points + constitution_bonus
    dict_player_stats.update({"hit_points": updated_hitpoints})
    print(text_color_green + f"Player Constitution Bonus: {dict_player_stats["constitution_bonus"]}\n" + text_end)

    player_armor_defence = dict_player_equipment["armor"]
    player_defense = 10 + dict_player_stats["dexterity_bonus"] + dict_armors[player_armor_defence][0]
    dict_player_stats.update({"player_defense_rating": player_defense})
    print(text_color_orange + f"Player Defence Rating: {dict_player_stats["player_defense_rating"]}\n" + text_end)

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
        for key, value in dict_player_equipment.items():
            print(f"{key}: {value}")

    # Display the list of options a player can do.
    def player_menu_main(self):
        print("Select from the options below:")
        for key, value in dict_menu_main.items():
            print(f"{key}: {value}", end="  ")
        character_selection = input("\n: ")
        return character_selection.upper()
    
    # Display the list of options a player can do during a fight
    def player_menu_fight(self):
        print("Select from the options below:")
        for key, value in dict_menu_fight.items():
            print(f"{key}: {value}", end="  ")
        character_selection = input(":")
        if character_selection.upper() == "A":
            player_character.attack("melee")
        elif character_selection.upper() == "D":
            player_character.attack("ranged")
        elif character_selection.upper() == "Q":
            print("You quaff a potion")
        elif character_selection.upper() == "F":
            print("You run away in terror.")

        #return character_selection.upper()
    
    # Attack Code using the standard D20 system. Roll 1d20 + attack bonus + attack stat bonus >= Defenders Defence/AC rating.

    def attack(self, attack_type):
        self.attack_type = attack_type
        if attack_type == "melee":
            if dict_player_equipment["weapon_melee"] == "none":
                print("You are not currently holding a melee weapon")
                to_hit_monster = 0
            else:
                print(f"You attack a {enemy.name} with your {dict_player_equipment["weapon_melee"]}")
                die_roll = Roll_Dice(1, 20)
                attack_bonus = player_character.player_attack_bonus + player_character.strength_bonus
                print(f"\nPlayer Attack Bonus = {player_character.player_attack_bonus}\n\nPlayer Strength Bonus = {player_character.strength_bonus}")
                to_hit_monster = die_roll + attack_bonus
                print(f"Total Attack Roll: {to_hit_monster}")
        else:
            if dict_player_equipment["weapon_ranged"] == "none":
                print("You are not currently holding a ranged weapon.")
                to_hit_monster = 0
            else:
                print(f"You attack a {enemy.name} with your {dict_player_equipment["weapon_ranged"]}")
                die_roll = Roll_Dice(1, 20)
                attack_bonus = player_character.player_attack_bonus + player_character.dexterity_bonus
                to_hit_monster = die_roll + attack_bonus
                print(f"Total Attack Roll: {to_hit_monster}")
        return to_hit_monster


    
    player_armor_defence = dict_player_equipment["armor"]
    player_defense = 10 + dict_player_stats["dexterity_bonus"] + dict_armors[player_armor_defence][0]
    dict_player_stats.update({"player_defense_rating": player_defense})
    #print(text_color_orange + f"Player Defence Rating: {dict_player_stats["player_defense_rating"]}" + text_end)


player_character = Player(dict_player_stats)

# This section is just for testing to make sure that the fields are being properly set.
'''print("Testing the menu display options")
player_character.player_menu_main()
print(" ")
print("Testing the check inventory function.")
player_character.check_inventory()

    def move():
        pass

    def open():
        pass
'''
# Random monster generator. This is to randomly select one of the mobs in the dict_monsters dictionary.

def random_monster():
    mob = dict_monsters[Roll_Dice(1, len(dict_monsters), True)]
    mob = globals()[mob]
    return mob
    


class Monster:
    def __init__(self, mob):
        for key, value in mob.items():
            setattr(self, key, value)
    
    def attack(self):
        print(f"A {enemy.name} viciously attacks you.")
        die_roll = Roll_Dice(1, 20, True)
        to_hit_player = die_roll + enemy.to_hit
        print(f"Enemy's To Hit = {enemy.to_hit}")
        return to_hit_player

# Test mobs


#mob = random_monster()
#enemy = Monster(mob)

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
                equiped_weapon = dict_player_equipment["weapon_melee"]
                ability_modifier = player_character.strength_bonus
            elif attack_type == "ranged":
                equiped_weapon = dict_player_equipment["weapon_ranged"]
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
    print("Your current stats bonuses are as follows:\n" + text_color_red + f"Strength:\t{dict_player_stats['strength_bonus']}" + text_end + text_color_blue + f"\nDexterity:\t{dict_player_stats['dexterity_bonus']}" + text_end + text_color_green + f"\nConstitution:\t{dict_player_stats['constitution_bonus']}" + text_end + "\n")
    player_character.check_inventory()

# Method to center the text in the screen based on the longest line.
def center_text(text, width=-1):
  lines = text.split('\n')
  width = max(map(len, lines)) if width == -1 else width
  return '\n'.join(line.center(width) for line in lines)


# Main code below here.
##### Main #####

#os.system('cls' if os.name == 'nt' else 'clear')

# The story thus far ...


print(center_text(text_color_cyan + "Welcome adventurer!\n\nWelcome to your final days.\n\nYou have become the latest test subject of the mad wizard Professor Bon Von Jovian" + text_end, 80))

print(text_color_blue + """
  
      
You have awoken in a cold, dark, and musty room.
The only sound is that of the dripping of water in the distance.
As your vision clears and you shake the cobwebs from your head, you begin
to recall the events leading up to this point. You were at an office party when 
you started to feel ill. You remember someone claiming to be a doctor had offered
to help you. Your world faded to black after accepting his help.""" + text_end)

input("Press " + text_color_blue + text_invert + "'Enter'" + text_end + " when you are ready to move on.\n\n")


input(f"Before you can gather your wits about you, time slows to a stop and you are transported to an empty white void . . .\n\nYou blink your eyes a couple of times as they adjust to the void white space.\nThis space is devoid of any features to the point to where you can't tell the difference between the walls, floor, and ceiling\n(If there are walls and a ceiling). You are suddenly started by the sudden appearance of the {text_color_purple}'Guiding Force'{text_end}. It has an androngenous appearance although the form is slightly feminie with a dual tone voice in unison, one feminine, the other masculine, as the {text_color_purple}'Guiding Force'{text_end} seems to whisper directly into your mind\n{text_color_purple}'Remember to just breathe. This is your inner soul space where . . . \nthe form fades away from your left side \nand reapears on your right side . . .\n'This is the space where you will increase your physical attributes.'\n'{text_end} and the {text_color_purple}'Guiding Force'{text_end} dissappears as quickly as it appeared. When you have collected your thoughs,\nPress " + text_color_green + text_invert + "'Enter'" + text_end + " to continue:\n\n")

print("One more thing ...\n")
# time.sleep(1)
print("The only way out is ahead of you.\n\n")
# time.sleep(2)
print("You can go forward.\n")
# time.sleep(2)
print("You can go left.\n")
# time.sleep(2)
print("You can go right.\n")
# time.sleep(2)
print("Heck, you can even go turn around and go back the way you came.\n\n")
# time.sleep(3)
print(text_color_red + "But you should" + text_invert + " NEVER " + text_end + text_color_red + "go back the way you came!\n\n" + text_end)
# time.sleep(3)
print("Let that sink into your pretty little noggin for a moment.\n\nYou can nod your pretty little head in agreement once your new reality has sunken in...")
# time.sleep(1)
input(center_text("\nBy pressing " + text_color_green + text_invert + "'Enter'" + text_end + " to continue: \n"))
# time.sleep(1)
print("\n\nTake a breath, don't stress, and remember ...\n")
# time.sleep(1)
print("...\n\n")
# time.sleep(1)
print("Don't say that ...\n")
# time.sleep(1)
print("Yooouuuuu ...\n")
# time.sleep(1)
print("Were ...\n")
# time.sleep(1)
print("NOT ...\n")
# time.sleep(1)
print(text_color_red + "WARNED!!!\n" + text_end)
# time.sleep(1)
print("\n\n")

character_creation()

increase_stats(player_remaining_stat_points)
update_stat_bonuses()
current_stats_and_inventory()

input(center_text("\n\nThis is where the adventure begins.\n\nYou poor, poor, lost test subje ... err ...\nI meant soul, you poor, poor, lost soul.\n\nPress 'Enter' to continue with your adventure.\n"))

enemy = Monster(dict_giant_rat)


# Random room description text and possiblity of encountering an enemy in the room. initially set at 18% of encountering an enemy.
# dict_menu_main = {"w": "Move forward", "a": "Go left", "s": "Turn back", "d": "Go right", "c": "Character sheet", "i": "Inventory", "q": "Quaff a Potion", "l": "Look Around"}

#my_test_variable = input(text_color_orange + dict_menu_main + text_end)
#actual_input = my_test_variable.upper()
#print(f"The character menu list is as follows:\n{actual_input}\n\n")
'''
player_menu_list = ""
for key, value in dict_menu_list.items():
    #menu_section = key + ","
    #player_menu_list += 
    print(key, ' : ', value)
'''


def fight(player_character, enemy, attack_type = "none"):
    fight_round = 1
    while player_character.is_alive and enemy.is_alive:
        if fight_round % 2 == 1:
            fight_choice = input("'A'ttack, 'Q'uaff a Potion, or 'F'lee?\n")
            if fight_choice.upper() == "A":
                fight_club(player_character, attack_type)
            elif fight_choice.upper() == "Q":
                print("You quaff a potion to regain some health:\n")
            elif fight_choice.upper() == "F":
                print("Those who fight and run away,\nlive to fight another day.\n\n")
                break
            else:
                print("You did not choose a valid option.\n")
                
        else:
            fight_club(enemy)
            fight_round += 1
            print(f"You fought for {fight_round} rounds.\n")

print(text_color_blue + """\n
As you look around the room you see that you are in a small rectangular room
made with rough stone walls and at one time it looks to have been a pantry. As you
investigate the supposed pantry, you realize that you are only wearing some very basic garments. No, make that more like dirty rags. What'ev ... as you look around the room you find an old chef's knife. While lost in thought wondering who would have left such a rusted piece of junk here you snap out of your thoughts as an 'R' 'O' 'U' 'S' or Rodent of Unusual Size scurries across the floor and glares at you hungrily eliciting a not so small yelping from you. You hear the juxting of the rather large, and sharp looking teeth as the, 'R' 'O' 'U' 'S' or ... in laymen's terms ... a giant rat prepares to make a meal out of your leg. You grab the rusty chef's knife and ...
      
You prepare to fight, because one of you two is on the menu for supper tonight.
And I don't think that you want it to be you that's on the menu tonight \ today, you know you can't tell what time of day it is here while trapped in this area as there are no windows or any indicators as to whether it is day or night outside of this place.\n""" + text_end)


print("You decide that it won't be you that's on the dinner menu for tonight.\n\n")

# Testing the fight mechanics. setup first fight here. Then random fights else where.
fight(player_character, enemy, "melee")

# player_character.player_menu_main()

def room_description():
    random_room_number = random.choice(list(dict_room_descriptions.keys()))
    print(f"As you enter the new room and gather your bearings: \n\n{dict_room_descriptions[random_room_number]}")

def monster_chance():
    # I am going to aim for a 30% chance of encountering a enemy
    monster_chance = Roll_Dice(1, 100, True)
    if monster_chance <= 30:
        monster_in_room = True
        return monster_in_room
    else:
        print("There was no monster to greet you.")


def main():
    print("************")
    room_description()
    monster_chance()
    if monster_in_room:
        mob = random_monster()
        enemy = Monster(mob)
        print(f"A {enemy.name} is poised, ready to strike!")
        player_character.player_menu_fight
    
    else:
        player_character.player_menu_main



    print("Generate if an enemy is in the room.")
    print("show player menu depending on if enemy is in room. Either standard menu or fight menu.")
    player_character.player_menu_main


main()
print("\n\nThis is the end of the file.\n\n")

input("Press " + text_invert + "'Enter'" + text_end + " to exit the game.")