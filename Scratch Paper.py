import os
import time
from turtle import clear

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

os.system('cls' if os.name == 'nt' else 'clear')
clear

print("Clearing the screen in . . .")
time.sleep(1)
print("3 . . .")
time.sleep(1)
print("2 . . .")
time.sleep(1)
print("1 . . .")
time.sleep(1)
print("CLEAR!")
time.sleep(2.5)

clear

# 'f' strings work for the typing speed.
string = (f"\n\n{text_color_cyan}{text_bold}Hey user whatup?{text_end} {text_color_green}\nWhere are you?{text_end}{text_invert}\nI am trying to debug this issue since I installed the update.{text_end}\n\n{text_underline}{text_color_blue}OK, this will be the{text_end}{text_color_blue}{text_invert} last sentences for testing {text_end}{text_underline}{text_color_green}and adding in colors.{text_end}")

# Concatanated strings do not work.
#string = ({text_color_purple} + "Howdy!" + {text_end} + {text_color_green} + {text_underline} + "\n\nThe End!" + {text_end} + {text_color_purple} + {text_bold} + "\n\nFIN")
for char in string:
    print(char, end='')
    time.sleep(.07)