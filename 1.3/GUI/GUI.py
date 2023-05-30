from tkinter import *
from tkinter import font
from GUI.login import Login
from GUI.Menu import Menu

from saf.GUI import GUI as gui_saf
from wpp.GUI import GUI as gui_wpp

class Application:

    def __init__(self, diretorio):
        # configurações de root
        self.root = Tk()
        self.bg_color = 'lightgray'
        self.width_height = (700, 600)
        self.root.iconbitmap(diretorio + '/images/icon.ico') # icone da janela
        self.root.resizable(False, False) # responsividade
        self.root.title('Central Suporte')
        self.root.config(background=self.bg_color)
        
        # variáveis de fluxo - utilizadas em outras funções e métodos
        self.users = ['HEVERTON', 'IAGO', '']
        self.button_color = '#bcbcbc'
        self.button_clicked_color = '#999999'

        # métodos da classe
        self.__centralize()
        self.__font()

        # instâncias e outras guias
        self.login()
        self.menu = Menu
        self.saf = gui_saf
        self.wpp = gui_wpp

    def __centralize(self):
        width, height = self.width_height

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        self.root.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))


    def __font(self):
        self.defaultFont = font.nametofont("TkDefaultFont") 
        self.defaultFont.configure(family="Bahnschrift SemiBold Condensed", size=15, weight=font.BOLD) 


    def _container_center(self): # utilizado para as subfunções (saf, bioac...)
        self.container_center = Frame(self.root)
        self.container_center.place(relx=0.15, rely=0, relheight=1, relwidth=0.85)
    
    def login(self):
        try:
            self.container_center.destroy() # caso já tenha sido executado, irá encerrar a janela para um novo login ao clicar em Sair
        except AttributeError:
            pass

        Login(self)