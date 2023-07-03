import os
from my_tools import reg_windows, reg
import winreg



if __name__ == '__main__':
    DESKTOP = reg_windows['DESKTOP']
    LOCALAPPDATA = reg_windows['LOCALAPPDATA']

    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\CentralSuporte')
    except FileNotFoundError:
        pass
    
    try:
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\CentralSuporte')
    except FileNotFoundError:
        pass