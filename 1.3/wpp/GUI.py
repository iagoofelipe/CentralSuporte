from tkinter import *

class GUI:
    def __init__(self, master):
        # elementos de root
        self.master = master
        self.root = master.root
        
        # elementos de botões
        self.button_color = self.master.button_color
        self.button_clicked_color = self.master.button_clicked_color

        # elementos de container que armazenará todos os widgets desta instância
        self.master._container_center()
        self.container_center = self.master.container_center
        self.container()
        self._container_valores()


    def container(self):
        Label(self.container_center, text='Removendo etiquetas e contabilizando os atendimentos.').place(relx=0.05, rely=0.03)

        Button(
            self.container_center, 
            text='INTERROMPER', 
            bd=0, 
            fg='white',  
            background='#444444', 
            activebackground=self.button_clicked_color,
            activeforeground='white'
            ).place(relx=0.05, rely=0.8)
        
        Button(
            self.container_center, 
            text='INICIAR', 
            bd=0, 
            fg='white',  
            background='#444444', 
            activebackground=self.button_clicked_color,
            activeforeground='white'
            ).place(relx=0.85, rely=0.8)
    

    def _container_valores(self):
        background = 'lightgray'
        self.container_valores = Frame(self.container_center, background=background)
        self.container_valores.place(relx=0.05, rely=0.15, relheight=0.55, relwidth=0.89)

        def line(relx, rely, relheight, relwidth): # padrão linha horizontal centralizada na tela
            Frame(self.container_valores, background='white').place(relx=relx, rely=rely, relheight=relheight, relwidth=relwidth)

        Label(self.container_valores, text='Atendentes', background=background).place(relx=0.15, rely=0.01)
        Label(self.container_valores, text='Contagem', background=background).place(relx=0.65, rely=0.01)
        

        line(relx=0.499, rely=0, relheight=1, relwidth=0.001)
        line(relx=0, rely=0.1, relheight=0.001, relwidth=1)

