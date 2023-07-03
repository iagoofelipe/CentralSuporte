""" 
Primeira execução, adiciona informações ao Registro do Windows, 
como __path__, build-version e entre outros.
"""
from my_tools import reg_windows, get_cfg, reg, resource_path, File
import os

cfg = get_cfg()

__version__ = cfg['last-version']
__path__ = os.path.join(reg_windows['LOCALAPPDATA'], 'CentralSuporte', '')
desktop_path = os.path.join(reg_windows['DESKTOP'], '')
files_path = os.path.join(__path__, 'Files', '')
server = r'\\TRUENAS\suporte\SUPORTE\CentralSuporte'
users = cfg['users']

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
    # os.system(r'xcopy {} {} /e /y'.format(resource_path('dependences' + __version__), __path__))

    File.toFile(__path__ + 'settings.json', settings_json)

    # atalho área de trabalho
    src = os.path.join(server, 'dependences', 'atendimentos' + __version__, 'dll', 'CentralSuporte.exe')
    dst = desktop_path + 'Central Suporte'

    try:
        os.symlink(src, dst)
    except:
        pass