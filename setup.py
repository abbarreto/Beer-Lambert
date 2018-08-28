#import sys
from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["tkinter", "serial", "numpy", "math", "matplotlib"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
baseOS = None
if sys.platform == "win32":
    baseOS = "Win32GUI"
    
setup(
    name = "GUILambert",
    version = "0.1",
    description = "Minha aplicacao GUI",
    options = {"build_exe": build_exe_options},
    executables = [Executable("GuiLambertv1.py",base=baseOS)]
    )
