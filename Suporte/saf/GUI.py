""" 
interface principal, cria e conecta as demais estruturas de interface SAF

required : ..GUI
requested : 
            master(
            root, button_color, button_clicked_color
            )

"""

# módulos Python
from tkinter import *
import pyautogui as ag

# subprocessos
from .__main__ import Saf
from .fbutton import verificar, cadastrar, adicionar, continuar
from .bind import bind_manualmente, bind_verificar

from ..bitrix import Bitrix
from ..__init import delFile

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

        self.main_saf = Saf()
        self.bitrix = Bitrix()
        self.__error()

    def __error(self):
        """ impedindo execução caso ocorra algum erro, como FileNotFoundError """
        if self.main_saf.error:
            pass
        else:
            self.master._container_center() # utilizado para criar um novo Frame para widgets do SAF
            self.container_center = self.master.container_center
            self._container()


    def _container(self):
        # widgets principais
        self.frame_saf = Label(self.container_center, text='Clique na opção desejada:')
        self.frame_saf.place(relx=0.1, rely=0.05)
        

        # botões
        btn_cadastrar = Button(self.container_center, self.btn_parametros, text='CADASTRAR')
        btn_cadastrar['command'] = self.fbutton_cadastrar
        btn_cadastrar.place(relheight=0.1, relwidth=0.3, rely=0.384, relx=0.35)

        btn_verificar = Button(self.container_center, self.btn_parametros, text='VERIFICAR')
        btn_verificar['command'] = self.fbutton_verificar
        btn_verificar.place(relheight=0.1, relwidth=0.3, rely=0.5, relx=0.35)

    # funções de botões
    def fbutton_verificar(self):
        verificar(self)
    
    def fbutton_cadastrar(self):
        # ag.alert('Em desenvolvimento :)')
        # cadastrar(self)
        print(delFile('aaa.a'))

    def fbutton_adicionar(self):
        adicionar(self)

    def fbutton_continuar(self):
        continuar(self)
    
    # binds
    def bind_manualmente(self, event):
        bind_manualmente(self, event)

    def bind_verificar(self, event):
        bind_verificar(self, event)