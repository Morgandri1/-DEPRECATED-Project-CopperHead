import pyfiglet
from colorama import Fore as colour, Back as back
import itertools
import threading
import time as Time
import sys
import asyncio # used for app class. might never be implimented though.

# color variables because of course colorama's color names have to be in caps
red = colour.RED
yellow = colour.YELLOW
blue = colour.CYAN
black = colour.BLACK
green = colour.GREEN
white = colour.WHITE
magenta = colour.MAGENTA
reset_color = colour.RESET

DEFAULT_FONT = 'standard' # pyfiglet banner font

back_red = back.RED
back_yellow = back.YELLOW
back_blue = back.BLUE
back_black = back.BLACK
back_green = back.GREEN
back_white = back.WHITE
back_magenta = back.MAGENTA
reset_back = back.RESET

false = False # i swear this trips me up so much and it annoys me so im making a namespace for it

def prompt(color = reset_color, text = "press enter to continue"):
    """creates a no-input continue prompt."""
    value = input(color + f"{text} ")
    if value == "":
        return
    else:
        print("No input required!")
        prompt(text)

def banner(color = reset_color, *, text, font=DEFAULT_FONT):
    """creates a banner for your application"""
    banner = pyfiglet.figlet_format(text, font)
    print(color + banner)
    print(white)

def color_print(color, text):
    """makes colored text"""
    print(color + text + white)

def loading_bar(color=reset_color, text="loading...", time=1):
    """makes a little loading icon next to your inputed text, for however long you'd like it to wait."""
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write(color + f'\r{text} ' + c)
            sys.stdout.flush()
            Time.sleep(0.1)
        sys.stdout.write(color + '\rDone!')

    t = threading.Thread(target=animate)
    t.daemon=True   # allows program to be stopped upon KeyboardInterrupt
    t.start()
    Time.sleep(int(time))
    done = True
    print(reset_color + "\ndone")

def rainbow_print(text="colors", time=5):
    """prints with **flare**"""
    done = False
    def animate():
        for c in itertools.cycle([f"{red+text}", f"{yellow+text}", f"{green+text}", f"{blue+text}", f"{magenta+text}", f"{black+text}"]):
            if done:
                break
            sys.stdout.write(f'\r'+c)
            sys.stdout.flush()
            Time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.daemon=True   # allows program to be stopped upon KeyboardInterrupt
    t.start()
    Time.sleep(int(time))
    done = True
    print(reset_color+"\r")

# -------- v2 line -------------
# class copperUI_app():
#     """a main app structure. all apps inherit from this. i have no idea what i'm doing here"""
#     def __init__(self):
#         colorama.init()
#         pass

#     @classmethod
#     def run(self, logging: bool = False):
#         """Runs everything in the app class"""
#         async def runner():
#             print("hello!")

#         try:
#             asyncio.run(runner())
#         except KeyboardInterrupt:
#             return
# -------- v2 line -------------

# might use that later ^^
# maybe not tho