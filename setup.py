import os

Macos_Prefix = "python3 -m "
packages = [
    "numpy",
    "colorama",
    "pyfiglet",
]

class setup():
    """main setup process"""
    def OS():
        """checks if you are using a unix based device or windows"""
        print(os.name)
        if os.name == "posix":
            setup.package_inst(systype="posix")
        else:
            setup.package_inst(systype="win")
            
    def package_inst(systype):
        """installs required dependencies"""
        if systype == "posix":
            for package in packages:
                os.system(f"{Macos_Prefix} pip install {package}") # installs all the copperUI dependencies. 
        elif systype == "win": 
            for package in packages:
                os.system(f"pip install {package}")