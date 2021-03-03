import sys
from cx_Freeze import setup, Executable
import os

build_exe_options = {"packages": ["os", "pygame"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

pygame_py_file = os.path.join('spaceshooter', 'spaceShooter.py')

setup(  name = "Space Shooter",
        version = "0.0.2",
        description = "classic retro game made using pygame",
        options = {"build_exe": build_exe_options},
        executables = [Executable(pygame_py_file, base=base)]
)