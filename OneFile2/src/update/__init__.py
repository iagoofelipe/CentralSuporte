import threading, time

from my_tools import File, Registros as reg
from src.update.gui_update import GIF

def check_update():
    registros = reg.get()
    server_ip = registros['server-id']

    if not File.isFile(r'{}\last_version.json'.format(server_ip)):
        return
        
    def update():
        thead = threading.Thread(target= lambda: GIF().loop())
        thead.start()

        for i in range(4):
            print(f'Atualizando arquivo: {i}')
            time.sleep(1)
        
        File.toFile(f'{__path__}end.txt', 'True')
        exit()

    __path__ = registros['__path__']
    __verion__ = registros['build-version']
    last_version = File.getFile(r'{}\last_version.json'.format(server_ip))['build-version']

    if last_version not in (None, __verion__): # irá atualizar apenas se for reconhecido o arquivo last_version.json e for diferente da versão instalada
        update()