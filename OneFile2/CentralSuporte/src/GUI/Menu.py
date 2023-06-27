""" 
interface de menu sidebar, possui botões para as principais funcionalidades

required : .GUI
requested : master(
                root, 
                user, button_color, button_clicked_color,
                saf .saf.GUI, 
                atendimentos .atendimentos
                ) <object>

"""

from tkinter import *
import pyautogui as ag
from my_tools import Registros as reg

__version__ = reg.get(nome='build-version')
text = f"""Build version: {__version__}

Developed by Iago Carvalho
"""

class Menu:
    def __init__(self, master):
        # configurações de root e janelas
        self.master = master
        self.root = master.root
        self.user = master.user

        # elementos de botões
        self.button_color = self.master.button_color
        self.button_clicked_color = self.master.button_clicked_color

        # chamativa de métodos
        self.__container()

    def desenvolvimento(self):
        ag.alert('Em desenvolvimento :)')

    def __container(self):
        backgroud = '#444444'

        # container com widgets de Menu
        self.menu = Frame(self.root, background=backgroud)
        self.menu.place(relx=0, rely=0, relheight=1, relwidth=0.15)

        Label(self.menu, text=f'Usuário:\n{self.user}', justify='left', background=backgroud, fg='white').place(relx=0.01, rely=0.03)

        # botões
        self.buttons_container = Frame(self.menu, background='white')
        self.buttons_container.place(relheight=0.452, relwidth=1, rely=0.274)

        self.button_saf = Button(self.buttons_container, text='SAF', bd=0, background=self.button_color, activebackground=self.button_clicked_color, command=self.desenvolvimento)
        self.button_saf.place(relheight=0.35, relwidth=1, rely=0)
        
        self.button_bioac = Button(self.buttons_container, text='BioAC', bd=0, background=self.button_color, activebackground=self.button_clicked_color, command=self.desenvolvimento)
        self.button_bioac.place(relheight=0.30, relwidth=1, rely=0.355)

        self.button_atendimentos = Button(self.buttons_container, text='Atendimentos', bd=0, background=self.button_color, activebackground=self.button_clicked_color, command=self.atendimentos)
        self.button_atendimentos.place(relheight=0.35, relwidth=1, rely=0.66)

        Button(self.menu, text='sair', justify='right', background=backgroud, fg='white', bd=0, command=self.master.login).place(relx=0.05, rely=0.88)
        Button(self.menu, text='sobre', justify='right', background=backgroud, fg='white', bd=0, command=self.sobre).place(relx=0.05, rely=0.93)

    def sobre(self):
        ag.alert(text)

    def saf(self):
        self.master.saf(self.master)

    def bioac(self):
        pass

    def atendimentos(self):
        self.master.atendimentos(self.master)