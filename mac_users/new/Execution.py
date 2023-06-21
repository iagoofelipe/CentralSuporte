from datetime import datetime
from pyautogui import alert
import os

from my_tools import File, resource_path, encode
from src.App import App
from src.sincronizar import sincronizar


class Execution:
    def __init__(self):
        self.file = File()
        self.path = self.file.path
        self.files_path = self.path + r'\files'
        self.date = str(datetime.now())

        self.make_files()


    def make_files(self):
        """ criando arquivos necessários """
        if not self.file.isFile(self.files_path):
            os.mkdir(self.path + r'\files')

        os.system(r'getmac /fo csv > {}\files\mac.txt'.format(self.path))
        os.system(r'net localgroup Administradores > {}\files\administradores.txt'.format(self.path))
        os.system(r'net localgroup Usuários > {}\files\usuarios.txt'.format(self.path))


    def getCpf(self):
        app = App()
        app.root.mainloop()
        cpf = app.cpf

        if cpf == None: # caso o cpf não seja coletado
            exit()
        
        return cpf

    def __call__(self):
        mac_file = self.file.getFile(self.files_path + r'\files\mac.txt')
        adm_file = self.file.getFile(self.files_path + r'\files\administradores.txt')
        user_file = self.file.getFile(self.files_path + r'\files\usuarios.txt')

        mac, user = [], []
        cpf = self.getCpf()
        adm = adm_file[6:-2]
        concatenar = lambda lista: encode('     '.join(lista), upper=False)

        for i in mac_file[1:]:
            i = i.split(',')[0]
            i = i.replace('"', '')
            mac.append(i)
        
        for i in user_file[6:-2]:
            if 'AUTORIDADE' not in i:
                user.append(i)

        sincronizar([cpf, self.date, concatenar(mac), concatenar(adm), concatenar(user)])
        os.system('rmdir /s /q files')
        alert('Dados sincronizados com êxito!')