import time

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

string = (f"{text_color_cyan}{text_bold}Hey user whatup? Where are you! I am trying to debug this issue since I installed the update.jas3kljowijt;asd awstUZIPjkasfmpipwe. asdat as .as  datw.t24t zgf x. aseddoiljmnasvosehseovl;asgo   hsreo h{text_end}")
for char in string:
    print(char, end='')
    time.sleep(.07)