from info import *
from copperhead import *
from sys import argv as arg
from colorama import Fore, Back

def list():
    prompt(color=red, text="this command lists *all* fonts usable with the banner function. the list is very long.\n\n press enter to continue...")
    print("\n".join(fonts))

def help():
    print(f"""
    CLI:
        -f -> shows all font options for banner()
        help -> displays this message
    Functions and values
        all text based functions share at least 2 common args;
            text: this one is pretty obvious. there is not a default value for this on any function besides prompt.
            color: this is defaulted to whatever color your CLI interface is. 
        
        color options:
            red,
            blue,
            black,
            green,
            white (more of an off gray),
            magenta.
        
        banner documentation:
            banner has the standard options first, and then font. font options can be found by running {Back.CYAN}python3 -m copperhead -f {Back.RESET}
    """)
    prompt()

if arg[1] == "-f":
    list()
elif arg[1] == "-h":
    help()