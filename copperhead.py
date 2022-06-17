import pyfiglet # used for banner
from colorama import Fore as colour, Back as back # used for text functions 
import itertools # used for waiting stuff
import threading # used for waiting stuff
from time import sleep as Time # used for waiting...
import sys # used for stdout
import asyncio # used for app class.
from playsound import playsound # its morbin time

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

def prompt(color = reset_color, text = "press enter to continue", background: str = ""):
    """creates a no-input continue prompt."""
    value = input(background + color + f"{text} " + reset_back)
    if value == "":
        return
    else:
        print("No input required!")
        prompt(color, text=text)

def banner(color = reset_color, *, text, font=DEFAULT_FONT, background: str = ""):
    """creates a banner for your application"""
    banner = pyfiglet.figlet_format(text, font)
    print(background + color + banner)
    print(reset_color + reset_back)

def color_print(color, text, background = ""):
    """makes colored text"""
    print(background + color + text + white + reset_back)

def loading(color=reset_color, text="loading...", time=1, background: str = ""):
    """makes a little loading icon next to your inputed text, for however long you'd like it to wait."""
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write(background + color + f'\r{text} ' + c)
            sys.stdout.flush()
            Time(0.1)
        sys.stdout.write(color + '\rDone!')

    t = threading.Thread(target=animate)
    t.daemon=True   # allows program to be stopped upon KeyboardInterrupt
    t.start()
    Time(int(time))
    done = True
    print(reset_color + reset_back + "\ndone")

def play(path, returns: bool = True):
    """plays a sound"""
    playsound(path)
    if returns == True:
        print(f"playing {path}...")
    else:
        return

def rainbow_print(text="colors", time=5):
    """prints with **flare**"""
    done = False
    def animate():
        for c in itertools.cycle([f"{red+text}", f"{yellow+text}", f"{green+text}", f"{blue+text}", f"{magenta+text}", f"{black+text}"]):
            if done:
                break
            sys.stdout.write(f'\r'+c)
            sys.stdout.flush()
            Time(0.1)

    t = threading.Thread(target=animate)
    t.daemon=True   # allows program to be stopped upon KeyboardInterrupt
    t.start()
    Time(int(time))
    done = True
    print(reset_color + reset_back +"\r")

class CopperApp():
    """App organization functions"""
    def run(Welcome_Screen: str, persistent: bool = False, startsound: str = None):
        """Runs the app. this has the benefit of cleaning up app structuring, such as exiting with KeyboardInterupt
        runs with asyncio. for single eventloop apps, use start.
        if you use run, make sure to define with async. otherwise, use start. 
        if you dont need async, start is probably your best option.
        Args:
            Welcome_Screen: this is where your main menu should be defined. add the menu's function name here.
            persistent: this is a true/false arg. this decides if your app will loop.
            startsound: this is where you put the path to a sound file you want to play on startup
        """

        async def run_app() -> None:
            try:
                if persistent == True:
                    while persistent == True:
                        if startsound != None:
                            playsound(startsound)
                        await Welcome_Screen()
                else: 
                    if startsound != None:
                        playsound(startsound)
                    await Welcome_Screen()
            except KeyboardInterrupt:
                print(reset_back + reset_color+"\nexiting... ")

        asyncio.run(run_app())

    def start(Welcome_Screen: str, persistent: bool = False, startsound: str = None):
        """single eventloop processing for CopperApp processes
        
        *not async*

        Args:
            Welcome_Screen: this is where your main menu should be defined. add the menu's function name here.
            persistent: this is a true/false arg. this decides if your app will loop.
            startsound: this is where you put the path to a sound file you want to play on startup"""
        try:
            if persistent == True:
                while persistent == True:
                    if startsound != None:
                        playsound(startsound)
                    Welcome_Screen()
            else:
                if startsound != None:
                        playsound(startsound)
                Welcome_Screen()
                
        except KeyboardInterrupt:
            print(reset_back + reset_color+"\nexiting... ")