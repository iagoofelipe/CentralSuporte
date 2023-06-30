import threading, time, os

from my_tools import File, Registros as reg
from src.update.gui_update import Update

registros = reg.get()
__path__ = registros['__path__']
__verion__ = registros['build-version']
server_ip = r'\\TRUENAS\suporte\Central Suporte'

if File.isFile(r'\\TRUENAS\suporte\Central Suporte\last_version.json'):
    last_version = File.getFile(r'\\TRUENAS\suporte\Central Suporte\last_version.json')

else:
    pass

atualizar = __verion__

thread_function_update = lambda: Update().loop()
thread_function_main = lambda: os.system(r'{}dll\CentralSuporte.exe'.format(__path__))


def update():
    if not atualizar:
        return

    thead = threading.Thread(target=thread_function_update)
    thead.start()

    for i in range(4):
        print(f'Atualizando arquivo: {i}')
        time.sleep(1)
    
    File.toFile(f'{__path__}end.txt', 'True')
    exit()