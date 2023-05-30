from tkinter import *

class Menu:
    def __init__(self, master):
        self.master = master
        self.root = master.root
        self.user = master.user

        self.__container()

    def __container(self):
        backgroud = '#444444'
        button_color = '#bcbcbc'
        button_clicked_color = '#999999'

        self.menu = Frame(self.root, background=backgroud)
        self.menu.place(relx=0, rely=0, relheight=1, relwidth=0.15)

        Label(self.menu, text=f'Usuário:\n{self.user}', justify='left', background=backgroud, fg='white').place(relx=0.01, rely=0.03)

        self.buttons_container = Frame(self.menu, background='white')
        self.buttons_container.place(relheight=0.452, relwidth=1, rely=0.274)

        self.button_saf = Button(self.buttons_container, text='SAF', bd=0, background=button_color, activebackground=button_clicked_color)
        self.button_saf.place(relheight=0.35, relwidth=1, rely=0)
        
        self.button_bioac = Button(self.buttons_container, text='BioAC', bd=0, background=button_color, activebackground=button_clicked_color)
        self.button_bioac.place(relheight=0.30, relwidth=1, rely=0.355)

        self.button_wpp = Button(self.buttons_container, text='WhatsApp', bd=0, background=button_color, activebackground=button_clicked_color)
        self.button_wpp.place(relheight=0.35, relwidth=1, rely=0.66)

        Button(self.menu, text='Sair', justify='right', background=backgroud, fg='white', bd=0).place(relx=0.05, rely=0.93)