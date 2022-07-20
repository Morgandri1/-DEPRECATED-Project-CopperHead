import pyfiglet # used for banner
from colorama import Fore as colour, Back as back # used for text functions 
import itertools # used for waiting stuff
import threading # used for waiting stuff
from time import sleep as Time # used for waiting...
import sys # used for stdout
import asyncio # used for app class, as well as async functions 
from playsound import playsound # its morbin time
from datetime import datetime # for clock function

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

def error(text, stripped):
    """makes an error print"""
    if stripped == False:
        print(f"❌ details: {text}")
    else:
        print(f"❌ {text}")

def passed(text, stripped: bool = True):
    """makes a pass print"""
    if stripped == False:
        print(f"✅ details: {text}")
    else:
        print(f"✅ {text}")

def prompt(color = reset_color, text = "press enter to continue",*, background = reset_back):
    """creates a no-input continue prompt."""
    value = input(background + color + f"{text} " + reset_back)
    if value == "":
        return
    else:
        print("No input required!")
        prompt(color, text=text)

def banner(color = green, *, text = "CopperHead", font=DEFAULT_FONT, background = reset_back, end="\n"):
    """creates a banner for your application"""
    banner = pyfiglet.figlet_format(text, font)
    print(background + color + banner)
    print(reset_color + reset_back, end='\n')

def color_print(color, text, background = reset_back):
    """makes colored text"""
    print(background + color + text + white + reset_back)

async def loading(color=reset_color, text="loading...", time=1, background = reset_back):
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

async def clock(format="24"):
    """creates a clock
    args:
        format: this decides if you want to print with the 12 or 24 hour time format
    """
    if format == 24:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            sys.stdout.write(str(current_time) + '\r')
            sys.stdout.flush()
    if format == 12:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            hours, minutes = current_time.split(':')
            hours = int(hours); minutes = int(minutes)
            if hours > 12:
                sys.stdout.write(f"{hours-12}:{minutes}" + '\r')
                sys.stdout.flush()

class CopperApp():
    """App organization functions"""
    async def run(func, persistent: bool = False, startsound: str = None):
        """Runs the app. this has the benefit of cleaning up app structuring, such as exiting with KeyboardInterupt
        runs with asyncio. for single eventloop apps, use start.
        if you use run, make sure to define with async. otherwise, use start. 
        if you dont need async, start is probably your best option.
        Args:
            func: this is where your main menu should be defined. add the menu's function name here.
            persistent: this is a true/false arg. this decides if your app will loop.
            startsound: this is where you put the path to a sound file you want to play on startup
        """

        async def run_app() -> None:
            try:
                if persistent == True:
                    while persistent == True:
                        if startsound != None:
                            playsound(startsound)
                        await func()
                else: 
                    if startsound != None:
                        playsound(startsound)
                    await func()
            except KeyboardInterrupt:
                print(reset_back + reset_color+"\nexiting... ")

        asyncio.run(run_app())

    def start(func, persistent: bool = False, startsound: str = None):
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
                    func()
            else:
                if startsound != None:
                        playsound(startsound)
                func()
                
        except KeyboardInterrupt:
            print(reset_back + reset_color+"\nexiting... ")