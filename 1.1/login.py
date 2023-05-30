from tkinter import *
from tkinter import font
from tkinter.ttk import *

class Application_login:

    def __init__(self):
        self.root = Tk()
        self.bg_color = 'lightgray'
        self.width_height = (700, 600)
        self.root.iconbitmap('images/icon.ico') # icone da janela
        self.root.resizable(False, False) # responsividade

        self.root.title('Central Suporte')
        self.root.config(background=self.bg_color)
        self.__centralize()
        self.__font()
        self.__container_login()

        self.root.mainloop()

    def __font(self):
        self.defaultFont = font.nametofont("TkDefaultFont") 
        self.defaultFont.configure(family="Bahnschrift SemiBold Condensed", size=25, weight=font.BOLD) 

    def __centralize(self):
        width, height = self.width_height

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        self.root.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))

    def __container_login(self):
        labelTop = Label(self.root, text="LOGIN", justify='center')
        labelTop.place(relx=0.3, rely=0.3)

        comboExample = Combobox(self.root, values=['Atendente', 'Iago', 'Samuel', 'Pedro', 'Heverton', 'João', 'Luan'], justify='center', width=50)
        comboExample.place(relx=0.3, rely=0.4)
        comboExample.current(0)

        # Button(self.root, justify='center', text='CADASTRAR', bd=0, background='#bcbcbc').place(relheight=0.1, relwidth=0.3, rely=0.384, relx=0.35)
        # self.button_enter = Button(self.root, text='Entrar', background='#bcbcbc')
        # self.button_enter.place(relx=0.3, rely=0.5)
        # self.button_enter['background'] = '#bcbcbc'

        
Application_login()

