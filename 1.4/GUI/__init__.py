# módulos Python
from tkinter import *
from tkinter import font

# subprocessos
from GUI.login import Login
from GUI.Menu import Menu

from saf.GUI import GUI as gui_saf
from atendimentos import GUI as gui_atendimentos

class Application:

    def __init__(self, obj):
        # configurações de root e janelas
        self.root = Tk()
        self.__geometry(700, 600)
        self.root.iconbitmap(obj.__path__ + '/images/icon.ico') # icone da janela
        self.root.resizable(False, False) # responsividade
        self.root.title('Central Suporte')
        self.bg_color = 'lightgray'
        self.root.config(background=self.bg_color)
        
        # elementos gerais
        self.users = ['HEVERTON', 'IAGO', '']
        self.button_color = '#bcbcbc'
        self.button_clicked_color = '#999999'
        self.font_name = None
        self.obj = obj
        self.__path__ = obj.__path__

        # métodos da classe
        self.__font()
        self.login() # primeiro layout a ser carregado

        # subprocessos e outras guias/layouts
        self.menu = Menu
        self.saf = gui_saf
        self.atendimentos = gui_atendimentos


    def __geometry(self, width, height):
        """ configurando tamanho e centralização da janela """

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        self.root.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))


    def __font(self):
        """ configurando elementos de fonte """

        self.defaultFont = font.nametofont("TkDefaultFont") 
        self.defaultFont.configure(family="Bahnschrift SemiBold Condensed", size=15, weight=font.BOLD) 
        self.font_name = self.defaultFont.actual()['family']


    def _container_center(self):
        """ widget para subprocessos (saf, bioac...), utilizado para iniciar subprocessos ou limpar fluxo de navegação """

        self.container_center = Frame(self.root)
        self.container_center.place(relx=0.15, rely=0, relheight=1, relwidth=0.85)
    

    def login(self):
        """ interface de login, utilizado ao iniciar a classe e com fbutton_sair """
        try:
            self.container_center.destroy() # caso já tenha sido executado, irá encerrar a janela para um novo login ao clicar em Sair
        except AttributeError:
            pass

        Login(self)