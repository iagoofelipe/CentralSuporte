from datetime import datetime
from pyautogui import alert
import os, subprocess as sub

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
        self.cpf = self.getCpf()


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


    def _tratando_dados(self, mac_file, adm_file, user_file):
        mac, user = [], []
        adm = adm_file[6:-2] if adm_file != None else None

        for i in mac_file[1:]:
            i = i.split(',')[0]
            i = i.replace('"', '')
            mac.append(i)
        
        for i in user_file[6:-2]:
            if 'AUTORIDADE' not in i:
                user.append(i)

        return mac, user, adm


    def __call__(self):
        mac_file = self.file.getFile(self.files_path + r'\mac.txt')
        adm_file = self.file.getFile(self.files_path + r'\administradores.txt')
        user_file = self.file.getFile(self.files_path + r'\usuarios.txt')

        concatenar = lambda lista: encode('     '.join(lista), upper=False)
        mac, user, adm = self._tratando_dados(mac_file, adm_file, user_file)

        sincronizar([self.cpf, self.date, concatenar(mac), concatenar(adm), concatenar(user)], resource_path('credentials.json'))
        os.system('rmdir /s /q files')
        alert('Dados sincronizados com êxito!')


    def except_execution(self):
        os.system('rmdir /s /q files')
        
        mac_file = sub.check_output(r'getmac /fo csv').decode('utf-8', errors='replace').split('\r\n')
        user_file = sub.check_output(r'net localgroup Usuários').decode('utf-8', errors='replace').split('\r\n')
        adm = sub.check_output(r'net localgroup Administradores').decode('utf-8', errors='replace').split('\r\n')
        mac, user, _ = self._tratando_dados(mac_file, None, user_file)

        dados = {
            'mac': mac,
            'adm': adm[7:-3],
            'user': user[:-1],
            'date_now': str(datetime.now()),
            'cpf': self.cpf,
        }

        self.file.toFile('settings.json', dados)

if __name__ == '__main__':
    exe = Execution()
    try:
        exe()
    except: # em caso de qualquer erro
        exe.except_execution()
        alert('Um erro ocorreu durante a extração de dados, envie para a equipe de Suporte o arquivo "settings.json" gerado!\n\nLocal do arquivo: ' + exe.path)
