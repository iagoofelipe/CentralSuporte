from tkinter import *
from tkinter.ttk import Combobox
from _all.Geral import Json

class GUI:
    def __init__(self, master):
        # configurações de root e janelas
        self.master = master
        self.root = master.root

        # elementos de botões
        self.button_color = self.master.button_color
        self.button_clicked_color = self.master.button_clicked_color

        # elementos de container que armazenará todos os widgets
        self.master._container_center()
        self.container_center = self.master.container_center
        self.container()


    def container(self):
        Label(self.container_center, text='Contabilizando os atendimentos por tipo.').place(relx=0.05, rely=0.03)
        Button(self.container_center, text='contabilizar', bd=0, fg='white', background='#444444', activebackground=self.button_clicked_color, activeforeground='white').place(relx=0.8, rely=0.8)

        Combobox(self.container_center, values=self.__combobox_values()).place(relx=0.05, rely=0.15, relwidth=0.9)
        Label(self.container_center, text='telefone:').place(relx=0.05, rely=0.25)
        Entry(self.container_center).place(relx=0.2, rely=0.26)


    def __combobox_values(self) -> list:
        retorno, num_key = [], 0
        combobox_values = Json.getJson(r'1.3\_all\_files\tipos_de_atendimentos.json')

        for key, items in combobox_values.items():
            num_key += 1
            num_item = 1

            retorno.append(f'{num_key} - {key}')

            for i in items:
                retorno.append(f'    {num_key}.{num_item} - {i}')
                num_item += 1
        
        return retorno

