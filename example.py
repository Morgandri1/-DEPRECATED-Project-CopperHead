from sympy import per
from copperhead import *
# from CopperUI import *

def menu():
    banner(color=green, text="Copperhead")
    color_print(color=red, text="hi")
    prompt(color=green)
    loading_bar(color=blue, text="loading...", time=1)
    print("no color here!")
    rainbow_print(text="test")
    color_print(color=white, text="hello", background=back_red)
    print("hello!")

CopperApp.run(Welcome_Screen=menu, persistent=False)