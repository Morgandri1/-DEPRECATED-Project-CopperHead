# from copperhead import *
from CopperUI import *

try:
    banner(color=green, text="copperhead")
    color_print(color=red, text="hi")
    prompt(color=red, text="tschuss")
    loading_bar(color=blue, text="loading...", time=10)
except KeyboardInterrupt: # i recommend this for all TUI apps, for cleanliness and no obvious traceback clouding stuff up. 
    exit()