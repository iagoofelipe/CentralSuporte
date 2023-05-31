# módulos Python
from tkinter import *

# subprocessos
from saf.main import Saf
from bitrix.main import Bitrix


class GUI:
    def __init__(self, master):
        # configurações de root e janelas
        self.master = master
        self.root = master.root
        
        # elementos de botões e outros
        self.button_color = master.button_color
        self.button_clicked_color = master.button_clicked_color
        self.dados = None
        self.btn_parametros = {
            'justify' : 'center', 
            'bd' : 0, 
            'background' : self.button_color,
            'activebackground' : self.button_clicked_color
            }

        self.main_saf = Saf(self)
        self.bitrix = Bitrix()
        self.__error()


    def __container(self):
        # widgets principais
        self.frame_saf = Label(self.container_center, text='Clique na opção desejada:')
        self.frame_saf.place(relx=0.1, rely=0.05)
        
        # botões
        btn_cadastrar = Button(self.container_center, self.btn_parametros, text='CADASTRAR')
        btn_cadastrar['command'] = self.fbutton_cadastrar_saf
        btn_cadastrar.place(relheight=0.1, relwidth=0.3, rely=0.384, relx=0.35)

        btn_verificar = Button(self.container_center, self.btn_parametros, text='VERIFICAR')
        btn_verificar['command'] = self.fbutton_verificar_saf
        btn_verificar.place(relheight=0.1, relwidth=0.3, rely=0.5, relx=0.35)


    def __error(self):
        """ interrompendo em caso de erro """
        if self.main_saf.error:
            pass
        else:
            self.master._container_center() # utilizado para criar um novo Frame para widgets do SAF
            self.container_center = self.master.container_center
            self.__container()