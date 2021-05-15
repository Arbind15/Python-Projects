import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],"include_files":["C:/Users/hp/AppData/Local/Programs/Python/Python37/DLLs/tcl86t.dll","C:/Users/hp/AppData/Local/Programs/Python/Python37/DLLs/tk86t.dll"
                                                         ]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r'C:\Users\hp\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\hp\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

setup(  name = "My player",
        version = "0.1",
        description = "MP3 Player",
        options = {"build_exe": build_exe_options},
        icon="icc.ico",
        executables = [Executable("te.py", base=base,icon="icc.ico")])