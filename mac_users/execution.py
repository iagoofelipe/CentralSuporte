import os, sys
from datetime import datetime
from pyautogui import alert

from tools import getFile, sincronizar, toString, App
from files import make_files

__path__ = os.path.abspath('')

if __name__ == '__main__':
    app = App()
    app.root.mainloop()
    make_files()

    mac_file = getFile(__path__ + r'\files\mac.txt')
    adm_file = getFile(__path__ + r'\files\administradores.txt')
    user_file = getFile(__path__ + r'\files\usuarios.txt')

    mac, user = [], []
    adm = adm_file[6:-2]
    try:
        cpf = app.cpf
    except AttributeError: # caso o usuário feche a janela antes de fornecer os dados
        os.system('rmdir /s /q files')
        sys.exit()

    # cpf = '06658659109'
    date_now = datetime.now()

    for i in mac_file[1:]:
        i = i.split(',')[0]
        i = i.replace('"', '')
        mac.append(i)
    
    for i in user_file[6:-2]:
        if 'AUTORIDADE' not in i:
            user.append(i)

    sincronizar([cpf, date_now, toString(mac), toString(adm), toString(user)])
    # print([cpf, str(date_now), toString(mac), toString(adm), toString(user)])
    os.system('rmdir /s /q files')
    alert('Dados sincronizados com êxito!')