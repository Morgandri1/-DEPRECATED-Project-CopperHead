from sympy import per
from copperhead import *
from sys import argv as arg
# from CopperUI import *

async def menu():
    banner(color=green, text="Copperhead")
    color_print(color=red, text="hi")
    prompt(color=green)
    loading_bar(color=blue, text="loading...", time=1)
    print("no color here!")
    rainbow_print(text="test")
    color_print(color=white, text="hello", background=back_red)
    print("hello!")

def home():
    banner(color=green, text="Copperhead")
    color_print(color=red, text="hi")
    prompt(color=green)
    loading_bar(color=blue, text="loading...", time=1)
    print("no color here!")
    rainbow_print(text="test")
    color_print(color=white, text="hello", background=back_red)
    print("hello!")

if arg[1] == "-a":
    CopperApp.run(Welcome_Screen=menu, persistent=False)
if arg[1] == "-s":
    CopperApp.start(Welcome_Screen=home, persistent=False)