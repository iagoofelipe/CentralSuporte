from tkinter import *
from my_tools import encode

class Login:
    def __init__(self, master):
        # configurações de root e janelas
        self.master = master
        self.root = master.root
        self.users = master.users  

        # elementos da classe
        self.font_name = master.font_name
        self.background = 'lightgray'

        # chamativa de métodos
        self.__container()
        
    def __container(self):
        self.container = Frame(self.root)
        self.container.place(relheight=1, relwidth=1)

        # container com widgets de login
        self.container_login = Frame(self.container, background=self.background, height=300, width=300)
        self.container_login.pack(pady=100)

        # textos
        Label(self.container_login, text='LOGIN', background=self.background, font=(self.font_name, 20)).place(relx=0.25, rely=0.3)
        Label(self.container_login, text='Usuário', background=self.background, font=(self.font_name, 15)).place(relx=0.25, rely=0.45)

        # input nome usuário
        self.usuario = Entry(self.container_login, width=25)
        self.usuario.bind("<Return>", self.fbutton_entrar)
        self.usuario.place(relx=0.25, rely=0.55)

        # mensagem de erro
        self.error_label = Label(self.container_login, background=self.background, fg='red', font=(self.font_name, 11))
        self.error_label.place(relx=0.2, rely=0.62)
        
        Button(self.container_login, bd=0, text='Entrar', command=self.fbutton_entrar).place(relx=0.65, rely=0.8, relwidth=0.25)


    def fbutton_entrar(self, event=None):
        usuario = encode(self.usuario.get(), upper=True)

        if usuario not in self.users:
            self.error_label['text'] = 'Usuário incorreto ou não cadastrado!'

        else:
            self.container.destroy()
            self.master.user = usuario
            self.master.menu(self.master)