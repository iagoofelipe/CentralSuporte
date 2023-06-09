""" 
interface principal, cria o root de base

utilizado : CentralSuporte
requisitos : 
        <tools> Json, Registros
        <GUI class> Login, Menu

"""

# módulos Python
from tkinter import *
from tkinter import font

# subprocessos
from my_tools import Registros as reg

class Application:
    def __init__(self):
        self.__path__ = reg.get(nome='__path__')

        # configurações de root e janelas
        self.root = Tk()
        self.__geometry(700, 600)
        self.root.iconbitmap(self.__path__ + r'icon.ico') # icone da janela
        self.root.resizable(False, False) # responsividade
        self.root.title('Central Suporte')
        self.bg_color = 'lightgray'
        self.root.config(background=self.bg_color)
        
        # elementos gerais
        self.button_color = '#bcbcbc'
        self.button_clicked_color = '#999999'
        self.font_name = None

        # métodos da classe
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
        """ widget para subprocessos (saf, bioac...), utilizado para iniciar subprocessos ou limpar fluxo de navegação """

        self.container_center = Frame(self.root)
        self.container_center.place(relx=0.15, rely=0, relheight=1, relwidth=0.85)

    def texto(self):
        Label(self.container_center, text='teste').pack(anchor='center', side='right')

    def loop(self):
        self.root.mainloop()


class Teste(Application):
    def __init__(self):
        super().__init__()

        self.bg_color = 'red'

if __name__ == '__main__':
    # app = Application()
    # app.loop()

    app = Teste()
    app.loop()