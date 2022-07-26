class NameSpace(Exception):
    class BackgroundColorError(Exception):
        print("""
        for background color please use background specified colors 

        ex: back_red 
        """)
        pass

    class ForegroundColorError(Exception):
        print("""
        for foreground (text) color please use standard colors, without the 'back' prefix.

        ex: red
        """)
        pass

class ArgumentError(Exception):
    print("incorrect argument")
