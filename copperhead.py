import pyfiglet
from colorama import Fore as colour


red = colour.RED
blue = colour.CYAN
black = colour.BLACK
green = colour.GREEN
white = colour.WHITE

def prompt(color, text):
    """creates a no-input continue prompt."""
    value = input(color + f"{text} ")
    if value == "":
        return
    else:
        print("No input required!")
        prompt(text)

def banner(color, text):
    """creates a banner for your application"""
    banner = pyfiglet.figlet_format(text)
    print(color + banner)

def color_print(color, text):
    """makes colored text"""
    print(color + text)
