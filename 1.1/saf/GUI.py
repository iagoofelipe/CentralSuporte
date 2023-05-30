from tkinter import *
from tkinter import font

class GUI_saf:

    def __init__(self, master_class):
        self.master_class = master_class
        self.root = master_class.root
        self._frame_saf()


    def _frame_saf(self):
        self.container_center = self.master_class.container_center

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