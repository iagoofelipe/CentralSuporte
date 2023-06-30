""" 
Primeira execução, adiciona informações ao Registro do Windows, 
como __path__, build-version e entre outros.
"""

import os
from my_tools import File, resource_path, Registros as reg

__version__ = '1.0.1'
sys_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'CentralSuporte', '')
home_path = os.path.join(os.path.expanduser('~'), 'desktop', '')
files_path = os.path.join(sys_path, 'Files', '')
users = 'IAGO, HEVERTON, SAMUEL, JOAO, PEDRO'
server = r'\\TRUENAS\suporte\Central Suporte'

KEYNAME = 'HKLM\SOFTWARE\CentralSuporte'

settings_reg = {
    "build-version": __version__,
    "users": users,
    "__path__": sys_path,
    "files-path": files_path,
    "atendimentos-files": os.path.join(sys_path, 'Files', 'atendimentos', ''),
    'server-id': server,
}

settings_json = {
    "build-version": __version__,
    "users": users.split(', '),
    "__path__": sys_path,
    "files-path": files_path,
    "atendimentos-files": os.path.join(sys_path, 'Files', 'atendimentos', ''),
    "dll": {"atendimentos": ["credentials.json", "tipos_de_atendimentos.json"]},
    'KEYNAME': KEYNAME,
    'server-id': server,
}

if __name__ == '__main__':
    os.mkdir(sys_path) if not os.path.exists(sys_path) else None

    os.system(r'xcopy {} {} /e /y'.format(resource_path('dependences'), sys_path))
    reg.set(KEYNAME, dict=settings_reg)

    File.toFile(sys_path + 'settings.json', settings_json)

    # atalho área de trabalho
    src = r'{}dll\CentralSuporte.exe'.format(sys_path)
    dst = f'{home_path}Central Suporte'

    os.symlink(src, dst)