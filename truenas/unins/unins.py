import os
import winreg
from pyautogui import alert
from my_tools import reg_windows

def expect_pass(func, argvs):
    try:
        func(*argvs)
    except:
        pass

if __name__ == '__main__':
    DESKTOP = reg_windows['DESKTOP']
    LOCALAPPDATA = reg_windows['LOCALAPPDATA']

    if os.path.exists(LOCALAPPDATA + r'\CentralSuporte\Files\atendimentos\atendimentos_local.json'):
        alert('Foram identificados atendimentos não sincronizados, realiza a sincronização e tente novamente!')
        exit()

    expect_pass(winreg.DeleteKey, (winreg.HKEY_CURRENT_USER, r'SOFTWARE\CentralSuporte'))
    expect_pass(winreg.DeleteKey, (winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\CentralSuporte'))
    expect_pass(winreg.DeleteKey, (winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\CentralSuporte'))
    expect_pass(os.rmdir, DESKTOP + 'Central Suporte.symlink')
    expect_pass(os.rmdir, DESKTOP + 'Central Suporte.lnk')
