import os
from datetime import datetime

from tools import getFile, sincronizar, toString, App
from files import make_files

__path__ = os.path.abspath('')
# today = date.today()
# data_update = today.strftime("%d/%m/%Y")

if __name__ == '__main__':
    make_files()
    app = App()
    app.root.mainloop()

    mac_file = getFile(__path__ + r'\files\mac.txt')
    adm_file = getFile(__path__ + r'\files\administradores.txt')
    user_file = getFile(__path__ + r'\files\usuarios.txt')

    mac = []
    adm = adm_file[6:-2]
    user = user_file[6:-4]
    cpf = app.cpf
    date_now = datetime.now()

    for i in mac_file[1:]:
        i = i.split(',')[0]
        i = i.replace('"', '')
        mac.append(i)


    # sincronizar([toString(mac), toString(adm), toString(user), cpf, date_now])
    sincronizar([cpf, date_now, toString(mac), toString(adm), toString(user)])
    os.system('rmdir /s /q files')