import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],"include_files":["C:/Users/hp/AppData/Local/Programs/Python/Python37/DLLs/tcl86t.dll","C:/Users/hp/AppData/Local/Programs/Python/Python37/DLLs/tk86t.dll","D:/Documents/ttmpp/venv/Lib/site-packages/"
                                                         ]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r'C:\Users\hp\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\hp\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

setup(  name = "login",
        version = "0.1",
        description = "Login",
        options = {"build_exe": build_exe_options},
        icon="gov2.ico",
        executables = [Executable("temp_login.py", base=base)])