""" 
interface principal, cria o root de base

utilizado em CentralSuporte.py

"""

# módulos Python
from tkinter import *
from tkinter import font

class Application:
    def __init__(self, address_icon=None, resizable=(False, False), title='Teste'):
        # configurações de root e janelas
        self.root = Tk()
        self.root.iconbitmap(address_icon) if address_icon != None else None # icone da janela
        self.root.resizable(*resizable) # responsividade
        self.root.title(title)

        # métodos da classe
        self.__geometry(700, 600)
        self.__font()
        self._container_center()


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
        """ widget para subprocessos, utilizado para iniciar subprocessos ou limpar fluxo de navegação """

        self.container_center = Frame(self.root)
        self.container_center.place(relx=0.15, rely=0, relheight=1, relwidth=0.85)



    def loop(self):
        self.root.mainloop()