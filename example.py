from copperhead import *
# from CopperUI import *

try:
    banner(color=green, text="Copperhead")
    color_print(color=red, text="hi")
    prompt(color=green)
    loading_bar(color=blue, text="loading...", time=1)
    print("no color here!")
    rainbow_print(text="test")
except KeyboardInterrupt: # i recommend this for all TUI apps, for cleanliness and no obvious traceback clouding stuff up. 
    exit()