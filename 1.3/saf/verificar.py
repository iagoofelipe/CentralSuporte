from _all.Geral import toFile, getFile, isFile, format_cpf, validador_cpf
import pyautogui as ag
from tkinter import *

from saf.GUI import GUI

class __verificar(GUI):
    # bind
    def bind_verificar(self, event):
        """ bind utilizada para marcar apenas um checkbox por vez """
        
        self.from_bitrix.set(False)
        self.from_local.set(False)
        self.from_manualmente.set(False)

        try:
            self.button_adicionar.place_forget()
            self.entry_manualmente.place_forget()
        except AttributeError:
            pass


    def bind_manualmente(self, event):
        self.entry_manualmente = Entry(self.container_center)
        self.button_adicionar = Button(self.container_center, text='adicionar', font=('Calibri', 9, 'normal'), command=self.fbutton_adicionar)
        
        self.button_adicionar.place(relx=0.35, rely=0.49)
        self.entry_manualmente.place(relx=0.1, rely=0.5, relwidth=0.2)
        self.dados = []


    # função botões
    def fbutton_verificar_saf(self):
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


    def fbutton_cadastrar_saf(self):
        print('cadastrar saf')

    def fbutton_adicionar(self):
        """ utilizada em "Digitar manualmente" """
        cpf_entry = format_cpf(self.entry_manualmente.get())
        if not validador_cpf(cpf_entry):
            ag.alert('CPF inválido!')

        else:
            self.dados.append(cpf_entry)
            self.entry_manualmente.delete(0, END)


    def fbutton_continuar(self):
        def bitrix():
            self.root.withdraw()
            self.dados = self.bitrix.getValues(17)
            toFile('saf/_files/cpfs_para_verificar_saf.csv', self.dados)
            self.root.deiconify()
        
        if self.from_bitrix.get():
            self.dados = ['066.586.591-09']
            print(self.dados)

        elif self.from_local.get():
            fileName = 'saf/_files/cpfs_para_verificar_saf.csv'

            if isFile(fileName):
                self.dados = getFile(fileName)
            else:
                bitrix()

        elif self.from_manualmente.get():
            if self.dados != []:
                toFile('saf/_files/cpfs_para_verificar_saf.csv', self.dados)
            
        else:
            self.error_label['text'] = 'selecione uma das opções'

        if self.dados != None:
            if self.dados == []:
                ag.alert('Nenhum cpf adicionando!')
                return
            self.root.withdraw()
            self.main_saf.verificar(self.dados) # realiza a verificação, adiciona o atributo resultado_verificacao para sua própria classe
            toFile('saf/_files/resultado_verificacao.csv', self.main_saf.resultado_verificacao)
            ag.alert('A verificação obteve êxito!')
            self.master._container_center() # limpando container
            self.__container()
            self.root.deiconify()