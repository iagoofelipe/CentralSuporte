""" 
Primeira execução, adiciona informações ao Registro do Windows, 
como __path__, build-version e entre outros.
"""

import os
from my_tools import File, Registros as reg

__version__ = '1.0.0'
sys_path = os.path.join(os.path.expanduser('~'), 'CentralSuporte', '')
files_path = os.path.join(sys_path, 'Files', '')
home_path = os.path.join(os.path.expanduser('~'), 'desktop', '')

KEYNAME = 'HKLM\SOFTWARE\CentralSuporte'

settings = {
    "build-version": __version__,
    "__path__": sys_path,
    'home-path': home_path,
    "files-path": files_path,
    "dll": {"atendimentos": ["credentials.json", "tipos_de_atendimentos.json"]},
    'KEYNAME': KEYNAME
}


# if not os.path.exists(sys_path):
if True:
    os.mkdir(sys_path) if not os.path.exists(sys_path) else None
    os.mkdir(files_path) if not os.path.exists(sys_path) else None

    os.system(r'xcopy \\TRUENAS\certfy\config\Files\dependences {} /e'.format(files_path))
    reg.set(KEYNAME, dict=settings)

    File.toFile(sys_path + 'default.json', settings)