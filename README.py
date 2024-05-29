"""
This is my first portfolio project from Codecademy.com from their Computer Science course. I have completed their intro to programming using the Python language. Now I am attempting to put together everything that I have learned up to this point. I have been working on this bit by bit and slowly expanding each section until I am satisfied with the base functionality.

This project is called "Dungeon Crawl". It is a simple text adventure game where you are thrust into a damp and dark cellar where you must find and fight your way out to freedom. But be warned. You can never go back the way that you came from in this adventure. Or you can try to go back and see how it works out for you. <you hear the sounds of maniacal laughter fading into the distance>


My original notes are below:
These are my basic thoughts and notes for my first portfolio project.
I plan on designing a simple RPG dungeon crawl.
For simplicity sake, I will only have a single class and race. A human fighter.
Other races and classes may be implemented in at a later time.
The goal is to have a very basic combat system, item shop, and character advancement.
This is will be a short game.

The scope of the game is as follows:
The player will name their character, select gender, and select their starting stats based on
a stat pool that they can use to distribute to their characteristics.
The player can equip weapons and armor
Fight enemies
Run away
use potions to regain health
utilize a shop
Possibly even save their progress

The options will be menu driven allowing the player to select numbers and letters to interact
with the menus.

*** Characteristics ***
Strength = overall damage output and equipment weight that they can carry.
Constitution = overall hit points and resistance to damage.
Dexterity = gives a chance to dodge an attack.
Character level = increased through earning experience.
Experience = Earned from defeating monsters and completing tasks.
Gold = Who doesn't like some pocket change.

Synopsys: You were traveling and sought shelter in a nearby appearently abandonded castle.
You are greeted by the grounds keeper who offers you a meal.
You awaken in dungeon with only one option. To fight your way out in an attempt to
escape your prison.

The only way out is forward, never and I never go back the way you came.
"""

# Example of simplifying a class.
# https://stackoverflow.com/questions/1639174/creating-class-instance-properties-from-a-dictionary
class MyClass:
    def __init__(self, data_dict):
        for key, value in data_dict.items():
            setattr(self, key, value)

# Example usage:
data = {"name": "Alice", "age": 30}
my_instance = MyClass(data)
print(my_instance.name)  # Output: "Alice"
print(my_instance.age)   # Output: 30


'''
I am trying to decide if I should use a "Linear Progress" for determining the exp threashhold for the next level.
# Current Level + Next Level * 30 for example
Or if I should use a "Curved Progression" approach to leveling up the player.
# XP Required = a * (level**) + b * Level + c

Maybe I'll use this ... XP_TO_LEVEL = (XP_BASE * CURRENT_LEVEL) ^ SCALE
I changed the scale rate from 1.5 to 1.15 else the XP to the next level grew quickly out of hand.
'''
xp_to_level = (100 * 1) ^ 1.5
print(xp_to_level) 
