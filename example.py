from copperhead import *
# from CopperUI import *

try:
    banner(color=green, text="Copperhead")
    color_print(color=red, text="hi")
    prompt(color=green)
    loading_bar(color=blue, text="loading...", time=1)
    print("no color here!")
    rainbow_print(text="test")
    print("hello!")
except KeyboardInterrupt:
    pass