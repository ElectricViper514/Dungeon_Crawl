import math
level = 1
level_max = 30
xp_to_level = 0

print("The exp needed for level 1 is 0.")
while level < (level_max + 1):
    xp_to_level = (100 * level) ** 1.15
    exp = round(xp_to_level)
    print(f"Level {level}: XP needed to the next level is '{exp}'.")
    level += 1 