from sys import argv as arg
from CopperUI import *

async def menu():
    banner(color=green, text="Copperhead")
    color_print(color=red, text="hi")
    prompt(color=green)
    loading(color=blue, text="loading...", time=1)
    print("no color here!")
    rainbow_print(text="test")
    color_print(color=white, text="hello", background=back_red)
    print("hello!")

def home():
    banner(color=green, text="Copperhead")
    color_print(color=red, text="hi")
    prompt(color=green)
    loading(color=blue, text="loading...", time=1)
    print("no color here!")
    rainbow_print(text="test", time=1)
    color_print(color=white, text="hello", background=back_red)
    print("hello!")

if arg[1] == "-a":
    CopperApp.run(func=menu, persistent=False)
if arg[1] == "-s":
    CopperApp.start(func=home, persistent=False)