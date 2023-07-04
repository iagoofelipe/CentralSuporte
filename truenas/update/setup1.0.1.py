""" 
Primeira execução, adiciona informações ao Registro do Windows, 
como __path__, build-version e entre outros.
"""
from my_tools import reg_windows, get_cfg, reg, File
import os

cfg = get_cfg('\\Truenas\suporte\CentralSuporte\settings.cfg')

__version__ = '1.0.1' # cfg['last-version']
__path__ = os.path.join(reg_windows['LOCALAPPDATA'], 'CentralSuporte', '')
desktop_path = os.path.join(reg_windows['DESKTOP'], '')
files_path = os.path.join(__path__, 'Files', '')
server = r'\\TRUENAS\suporte\SUPORTE\CentralSuporte'
users = 'IAGO, SAMUEL, PEDRO, HEVERTON, JOAO' # cfg['users']

settings_json = {
    "build-version": __version__,
    "users": users.split(', '),
    "files-path": files_path,
    "atendimentos-files": os.path.join(__path__, 'Files', 'atendimentos', ''),
    "dll": {"atendimentos": ["credentials.json", "tipos_de_atendimentos.json"]}
}

if __name__ == '__main__':
    reg.set(
        __version__ = __version__,
        __path__ = __path__,
        desktop_path = desktop_path,
        users = users,
        server_id = server
        )
    
    if not os.path.exists(__path__):
        os.mkdir(__path__)

    if not os.path.exists(files_path):
        os.mkdir(files_path)
    
    os.system(r'xcopy {} {} /e /y'.format(f'{server}\\dependences{__version__}', __path__))
    File.toFile(__path__ + 'settings.json', settings_json)

    # atalho área de trabalho
    os.system(r'xcopy {} {} /e /y'.format(f'{server}\\dependences{__version__}\\CentralSuporte.lnk', desktop_path))
    