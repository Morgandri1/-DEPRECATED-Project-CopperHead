import os

Macos_Prefix = "python3 -m "
packages = [
    "numpy",
    "colorama",
    "flask",
    "requests",
]

class setup():
    systype = -1
    """main setup process"""
    def OS():
        """checks if you are using a unix based device or windows"""
        print(os.name)
        if os.name == "posix":
            setup.systype = "posix"
        else:
            setup.systype = "win"
            
    def package_inst():
        setup.OS()
        if setup.systype == "posix":
            for package in packages:
                os.system(f"{Macos_Prefix} pip install {package}")
        elif setup.systype == "win": 
            for package in packages:
                os.system(f"pip install {package}")

