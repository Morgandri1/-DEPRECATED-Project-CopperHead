import colorama
import pyfiglet
from colorama import Fore as colour
import itertools
import threading
import time as Time
import sys

# color variables because of course colorama's color names have to be in caps
red = colour.RED
blue = colour.CYAN
black = colour.BLACK
green = colour.GREEN
white = colour.WHITE
magenta = colour.MAGENTA
reset_color = colour.RESET

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

def loading_bar(color, text, time):
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

# maybe important?
colorama.init()
