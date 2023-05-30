from tkinter import *

class GUI:

    def __init__(self, master):
        self.master = master
        self.root = master.root
        
        
        self.master._container_center()
        self.container_center = self.master.container_center
        self.container()


    def container(self):

        button_color = '#bcbcbc'
        button_clicked_color = '#999999'

        self.frame_saf = Label(self.container_center, text='Clique na opção desejada:')
        self.frame_saf.place(relx=0.1, rely=0.05)

        Button(self.container_center, justify='center', text='CADASTRAR', bd=0, background=button_color, activebackground=button_clicked_color, command=self.cadastrar_saf).place(relheight=0.1, relwidth=0.3, rely=0.384, relx=0.35)
        Button(self.container_center, justify='center', text='VERIFICAR', bd=0, background=button_color, activebackground=button_clicked_color, command=self.verificar_saf).place(relheight=0.1, relwidth=0.3, rely=0.5, relx=0.35)


    def verificar_saf(self):
        print('verificar saf')


    def cadastrar_saf(self):
        print('cadastrar saf')