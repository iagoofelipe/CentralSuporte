from tkinter import *
import pyautogui as ag

from ..__init import toFile, getFile, isFile, validar, formatar

def verificar(self):
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
    self.error_label = Label(self.container_center, fg='red', font=('Bahnschrift Light Condensed', 11, 'normal'))
    self.error_label.place(relx=0.1, rely=0.27)

    op1.place(relx=0.1, rely=0.3)
    op2.place(relx=0.1, rely=0.35)
    op3.place(relx=0.1, rely=0.4)

    for i in [op1, op2, op3]:
        i.bind('<Button-1>', self.bind_verificar, add='+')

    op3.bind('<Button-1>', self.bind_manualmente, add='+')

    Button(self.container_center, self.btn_parametros, text='continuar', fg='white', background='#444444', activeforeground='white', command=self.fbutton_continuar).place(relx=0.8, rely=0.8)


def cadastrar(self):
    print('cadastrar saf')


def adicionar(self):
    """ utilizada em "Digitar manualmente" """
    cpf_entry = formatar(self.entry_manualmente.get())
    if not validar(cpf_entry):
        ag.alert('CPF inválido!')

    else:
        self.dados.append(cpf_entry)
        self.entry_manualmente.delete(0, END)


def continuar(self):
    fileName = 'saf/files/cpfs_para_verificar_saf.csv'

    def bitrix():
        self.root.withdraw()
        self.dados = self.bitrix.getValues(17)
        toFile(fileName, self.dados)
        self.root.deiconify()
    
    if self.from_bitrix.get():
        bitrix()

    elif self.from_local.get():

        if isFile(fileName):
            self.dados = getFile(fileName)
        else:
            bitrix()

    elif self.from_manualmente.get():
        if self.dados != []:
            toFile(fileName, self.dados)
        
    else:
        self.error_label['text'] = 'selecione uma das opções'

    if self.dados != None:
        if self.dados == []:
            ag.alert('Nenhum cpf adicionando!')
            return
        self.root.withdraw()
        self.main_saf.verificar(self.dados) # realiza a verificação, adiciona o atributo resultado_verificacao para sua própria classe
        toFile('saf/files/resultado_verificacao.csv', self.main_saf.resultado_verificacao)
        ag.alert('A verificação obteve êxito!')
        self.master._container_center() # limpando container
        self.__container()
        self.root.deiconify()