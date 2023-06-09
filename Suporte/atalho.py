""" 
utilizado após o registro do caminho
"""

from __init import Registros

reg = Registros()
dir_paths = reg.get()

desktop = dir_paths['desktop_path']
__path__ = dir_paths['path']

bat = [
    f'cd {__path__}\n',
    'py -m Suporte'
    ]

vbs = [
    'Dim wshShell\n',
    'Set wshShell = CreateObject("WScript.Shell")\n',
    f'wshShell.Run "{__path__}\executavel.bat", 0, false'
    ]

with open(__path__ + '\executavel.bat', 'w') as f:
    f.writelines(bat)

with open(desktop + '\Central Suporte.vbs', 'w') as f:
    f.writelines(vbs)