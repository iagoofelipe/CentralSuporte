from tkinter import *
# from saf.main import Main

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

        # self.main_saf = Main(master.obj)

    def container(self):
        # widgets principais
        self.frame_saf = Label(self.container_center, text='Clique na opção desejada:')
        self.frame_saf.place(relx=0.1, rely=0.05)

        btn_cadastrar = Button(self.container_center, justify='center', bd=0)
        btn_cadastrar['text'] = 'CADASTRAR'
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

    def verificar(self, event):
        
        self.from_bitrix.set(False)
        self.from_local.set(False)
        self.from_manualmente.set(False)

    def verificar_saf(self):
        self.master._container_center() # limpando container
        self.container_center = self.master.container_center

        self.from_bitrix = BooleanVar()
        self.from_local = BooleanVar()
        self.from_manualmente = BooleanVar()

        font = (self.master.font_name, 13, 'normal')
        
        op1 = Checkbutton(self.container_center, text='Utilizar dados do bitrix (novos dados)', variable=self.from_bitrix, font=font)
        op2 = Checkbutton(self.container_center, text='Utilizar dados locais (caso não haja histórico de consulta, será gerado)', variable=self.from_local, font=font)
        op3 = Checkbutton(self.container_center, text='Digitar manualmente', variable=self.from_manualmente, font=font)
        
        Label(self.container_center, text='Selecione a fonte de dados:').place(relx=0.05, rely=0.2)
        op1.place(relx=0.1, rely=0.3)
        op2.place(relx=0.1, rely=0.35)
        op3.place(relx=0.1, rely=0.4)

        op1.bind('<Button-1>', self.verificar, add='+')
        op2.bind('<Button-1>', self.verificar, add='+')
        op3.bind('<Button-1>', self.verificar, add='+')

        Button(self.container_center, text='continuar', bd=0, fg='white', background='#444444', activebackground=self.button_clicked_color, activeforeground='white', command=self.__continuar).place(relx=0.8, rely=0.8)

    def cadastrar_saf(self):
        print('cadastrar saf')

    def __continuar(self):
        self._from = {
            'bitrix': self.from_bitrix.get(),
            'local': self.from_local.get(),
            'manualmente': self.from_manualmente.get()
            }
        
        print(self._from)