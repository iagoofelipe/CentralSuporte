from tkinter import *

class GUI:

    def __init__(self, master):
        # configurações de root e janelas
        self.master = master
        self.root = master.root
        
        # elementos de botões
        self.button_color = master.button_color
        self.button_clicked_color = master.button_clicked_color

        self.master._container_center() # utilizado para criar um novo Frame para widgets do SAF
        self.container_center = self.master.container_center
        self.container()


    def container(self):
        # widgets principais
        self.frame_saf = Label(self.container_center, text='Clique na opção desejada:')
        self.frame_saf.place(relx=0.1, rely=0.05)

        btn_cadastrar = Button(self.container_center, justify='center', bd=0)
        btn_verificar['text'] = 'CADASTRAR'
        btn_cadastrar['background'] = self.button_color
        btn_cadastrar['activebackground'] = self.button_clicked_color
        btn_cadastrar['command'] = self.cadastrar_saf
        btn_cadastrar.place(relheight=0.1, relwidth=0.3, rely=0.384, relx=0.35)

        btn_verificar = Button(self.container_center, justify='center', bd=0)
        btn_verificar['text'] = 'VERIFICAR'
        btn_verificar['background'] = self.button_color
        btn_verificar['activebackground'] = self.button_clicked_color
        btn_verificar['command'] = self.verificar_saf
        btn_verificar.place(relheight=0.1, relwidth=0.3, rely=0.5, relx=0.35)

    def verificar_saf(self):
        print('verificar saf')


    def cadastrar_saf(self):
        print('cadastrar saf')