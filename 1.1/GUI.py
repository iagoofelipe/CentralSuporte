from tkinter import *
from tkinter import font

from saf.GUI import GUI_saf

class Application:

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

        self._container_center()
        self.__container_menu()

        self.root.mainloop()


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


    def _container_center(self):
        self.container_center = Frame(self.root)
        self.container_center.place(relx=0.15, rely=0, relheight=1, relwidth=0.85)


    def __container_menu(self):
        backgroud = '#444444'
        button_color = '#bcbcbc'
        button_clicked_color = '#999999'

        self.menu = Frame(self.root, background=backgroud)
        self.menu.place(relx=0, rely=0, relheight=1, relwidth=0.15)

        self.buttons_container = Frame(self.menu, background='white')
        self.buttons_container.place(relheight=0.452, relwidth=1, rely=0.274)

        self.button_saf = Button(self.buttons_container, justify='center', text='SAF', bd=0, background=button_color, activebackground=button_clicked_color, command=self._frame_saf)
        self.button_saf.place(relheight=0.35, relwidth=1, rely=0)
        
        self.button_bioac = Button(self.buttons_container, justify='center', text='BioAC', bd=0, background=button_color, activebackground=button_clicked_color, command=self._frame_bioac)
        self.button_bioac.place(relheight=0.30, relwidth=1, rely=0.355)

        self.button_wpp = Button(self.buttons_container, justify='center', text='WhatsApp', bd=0, background=button_color, activebackground=button_clicked_color)
        self.button_wpp.place(relheight=0.35, relwidth=1, rely=0.66)


    def _frame_saf(self):
        self.container_center.destroy()
        self._container_center()
        GUI_saf(self)


    def _frame_bioac(self):
        self.container_center.destroy()
        self._container_center()

        self.frame_bioac = Label(self.container_center, justify='center', text='OOOI BioAC')
        self.frame_bioac.place(relx=0.5, rely=0.5)


Application()