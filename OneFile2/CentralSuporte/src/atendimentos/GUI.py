# módulos Python
from datetime import datetime as dt
from tkinter.ttk import Combobox
import pyautogui as ag
from tkinter import *

# módulos locais
from tools import Json, isFile, __path__
from src.atendimentos.main import sincronizar

class GUI:
    def __init__(self, master):
        # arquivos, caminhos e dados de arquivos
        self.settings = Json.getJson(__path__ + 'settings.json')
        self.local_dir = self.settings["atendimentos-files"]
        self.fileName = self.local_dir + 'atendimentos_local.json'
        self.dados_atendimentos = Json.getJson(self.fileName)
        self.categoria = {}

        self.__ERROR()

        # configurações de root e janelas
        self.master = master
        self.root = master.root
        self.__path__ = __path__

        # elementos de botões
        self.font = ('Segoe UI', 10)
        self.button_color = self.master.button_color
        self.button_clicked_color = self.master.button_clicked_color

        # elementos de container que armazenará todos os widgets
        self.master._container_center()
        self.container_center = self.master.container_center
        self.container()
        self.user = master.user

        self.sincronizar = sincronizar
        

    def __ERROR(self):
        dlls = self.settings['dll']['atendimentos']
        for fileName in dlls:
            if not isFile(self.local_dir + fileName, diretorio_padrao=False):
                ag.alert(f'FileNotFoundError\n {self.local_dir + fileName}')
                raise FileNotFoundError


    def container(self):
        self.container_center.bind('<Return>', self.fbutton_contabilizar)

        Label(self.container_center, text='Contabilizando atendimentos.').place(relx=0.05, rely=0.03)
        Button(self.container_center, text='contabilizar', bd=0, fg='white', background='#444444', activebackground=self.button_clicked_color, activeforeground='white', command=self.fbutton_contabilizar).place(relx=0.8, rely=0.8)
        Button(self.container_center, text='sincronizar', bd=0, fg='white', background='#444444', activebackground=self.button_clicked_color, activeforeground='white', command=self.fbutton_sincronizar).place(relx=0.05, rely=0.8)

        self.tipo_atendimento = Combobox(self.container_center, values=self.__combobox_values(), font=self.font)
        self.tipo_atendimento.place(relx=0.05, rely=0.15, relwidth=0.9)
        
        Label(self.container_center, text='telefone:', font=self.font).place(relx=0.05, rely=0.26)
        self.telefone = Entry(self.container_center)
        self.telefone.place(relx=0.05, rely=0.3)
        self.telefone.bind('<Return>', self.fbutton_contabilizar)

        Label(self.container_center, text='descrição:', font=self.font).place(relx=0.05, rely=0.36)
        self.descricao = Entry(self.container_center, font=self.font, justify='left')
        self.descricao.place(relx=0.05, rely=0.4, relwidth=0.5)
        self.descricao.bind('<Return>', self.fbutton_contabilizar)

    def __combobox_values(self) -> list:
        retorno, num_key = [], 0
        combobox_values = Json.getJson(self.local_dir + 'tipos_de_atendimentos.json')

        for key, items in combobox_values.items():
            num_key += 1
            num_item = 1

            retorno.append(f'{num_key} - {key}')
            self.categoria[f'{num_key} - {key}'] = key

            for i in items:
                retorno.append(f'--{num_key}.{num_item} {i}')
                self.categoria[f'--{num_key}.{num_item} {i}'] = key
                num_item += 1
        
        return retorno
    
    def alert(self):
        Label(self.container_center, text='Os campos "tipo de atendimento" e "telefone" são obrigatórios!', fg='red', font=('Segoe UI', 9, 'bold')).place(relx=0.05, rely=0.1)


    def fbutton_sincronizar(self):
        self.root.withdraw()
        self.sincronizar(self.dados_atendimentos)
        self.root.deiconify()
        self.dados_atendimentos = None


    def fbutton_contabilizar(self, event=None):
        tipo_atendimento = self.tipo_atendimento.get()
        telefone = self.telefone.get()
        descricao = self.descricao.get()
        self.user = self.master.user

        if tipo_atendimento == '' or telefone == '':
            self.alert()
            return
        
        self.dados_atendimentos = Json.getJson(self.fileName)

        if self.dados_atendimentos == None:
            self.dados_atendimentos = {}

        zero_esquerda = lambda num: str(num).zfill(2)
        today = dt.today()
        key = str(len(self.dados_atendimentos))
        # date = f'{zero_esquerda(today.day)}/{zero_esquerda(today.month)}/{today.year}'
        date = f'{zero_esquerda(today.month)}/{zero_esquerda(today.day)}/{today.year}' # padrão norteamericano, para funcionar no Apps Script
        
        self.dados_atendimentos[key] = [self.user, tipo_atendimento, self.categoria[tipo_atendimento], telefone, descricao, date]

        Json.setJson(self.dados_atendimentos, self.fileName)

        self.tipo_atendimento.delete(0, END)
        self.telefone.delete(0, END)
        self.descricao.delete(0, END)