from tkinter import *
from tkinter import font

class Login:
    def __init__(self, master):
        # elementos root
        self.master = master
        self.root = master.root
        self.users = master.users

        # elementos de fonte
        self.defaultFont = master.defaultFont
        self.font_name = self.defaultFont.actual()['family']

        # chamativa de métodos
        self.__container()
        
    def __container(self):
        self.container = Frame(self.root)
        self.container.place(relheight=1, relwidth=1)
        background = 'lightgray'

        container_login = Frame(self.container, background=background)
        container_login.place(relx=1/4, rely=0.15, relheight=0.6, relwidth=1/2)

        Label(container_login, text='LOGIN', background=background, font=(self.font_name, 20)).place(relx=0.3, rely=0.3)
        Label(container_login, text='Usuário', background=background, font=(self.font_name, 15)).place(relx=0.3, rely=0.45)

        self.usuario = Entry(container_login, width=25)
        self.usuario.place(relx=0.3, rely=0.55)

        self.error_label = Label(container_login, background=background, fg='#65000b', font=(self.font_name, 11))
        self.error_label.place(relx=0.25, rely=0.62)
        
        Button(container_login, bd=0, text='Entrar', command=self.fbutton_entrar).place(relx=0.7, rely=0.8, relwidth=0.25)


    def fbutton_entrar(self):
        usuario = self.usuario.get().upper()

        if usuario not in self.users:
            self.error_label['text'] = 'Usuário incorreto ou não cadastrado!'

        else:
            self.container.destroy()
            self.master.user = usuario
            self.master.menu(self.master)

    

# Tk().configure()