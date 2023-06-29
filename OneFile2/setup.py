""" 
Primeira execução, adiciona informações ao Registro do Windows, 
como __path__, build-version e entre outros.
"""

import os
from my_tools import File, Registros as reg

__version__ = '1.0.0'
sys_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'CentralSuporte', '')
files_path = os.path.join(sys_path, 'Files', '')
users = 'IAGO, HEVERTON, SAMUEL, JOAO, PEDRO'

KEYNAME = 'HKLM\SOFTWARE\CentralSuporte'

settings_reg = {
    "build-version": __version__,
    "users": users,
    "__path__": sys_path,
    "files-path": files_path,
    "atendimentos-files": os.path.join(sys_path, 'Files', 'atendimentos', ''),
}

settings_json = {
    "build-version": __version__,
    "users": users.split(', '),
    "__path__": sys_path,
    "files-path": files_path,
    "atendimentos-files": os.path.join(sys_path, 'Files', 'atendimentos', ''),
    "dll": {"atendimentos": ["credentials.json", "tipos_de_atendimentos.json"]},
    'KEYNAME': KEYNAME
}

if __name__ == '__main__':
    os.mkdir(sys_path) if not os.path.exists(sys_path) else None

    os.system(r'xcopy dependences {} /e'.format(sys_path))
    reg.set(KEYNAME, dict=settings_reg)

    File.toFile(sys_path + 'settings.json', settings_json)