# módulos Python
from oauth2client.service_account import ServiceAccountCredentials
from tkinter.ttk import Combobox
from tkinter import *
import gspread

# módulos locais
from _all.File import Json

class GUI:
    def __init__(self, master):
        # configurações de root e janelas
        self.master = master
        self.root = master.root
        self.__path__ = master.__path__

        # elementos de botões
        self.font = ('Segoe UI', 10)
        self.button_color = self.master.button_color
        self.button_clicked_color = self.master.button_clicked_color

        # elementos de container que armazenará todos os widgets
        self.master._container_center()
        self.container_center = self.master.container_center
        self.container()
        self.user = master.user

        self.fileName = self.__path__ + '/atendimentos/files/atendimentos_local.json'
        self.dados_atendimentos = Json.getJson(self.fileName)


    def container(self):
        self.container_center.bind('<Return>', self.fbutton_contabilizar)

        Label(self.container_center, text='Contabilizando atendimentos.').place(relx=0.05, rely=0.03)
        Button(self.container_center, text='contabilizar', bd=0, fg='white', background='#444444', activebackground=self.button_clicked_color, activeforeground='white', command=self.fbutton_contabilizar).place(relx=0.8, rely=0.8)
        Button(self.container_center, text='sincronizar', bd=0, fg='white', background='#444444', activebackground=self.button_clicked_color, activeforeground='white', command=self.fbutton_sincronizar).place(relx=0.05, rely=0.8)

        self.tipo_atendimento = Combobox(self.container_center, values=self.__combobox_values(), font=self.font)
        self.tipo_atendimento.place(relx=0.05, rely=0.15, relwidth=0.9)
        
        Label(self.container_center, text='telefone:', font=self.font).place(relx=0.05, rely=0.26)
        self.telefone = Entry(self.container_center)
        self.telefone.place(relx=0.05, rely=0.3)

        Label(self.container_center, text='descrição:', font=self.font).place(relx=0.05, rely=0.36)
        self.descricao = Entry(self.container_center, font=self.font, justify='left')
        self.descricao.place(relx=0.05, rely=0.4, relwidth=0.5)


    def __combobox_values(self) -> list:
        retorno, num_key = [], 0
        combobox_values = Json.getJson(r'1.3\_all\_files\tipos_de_atendimentos.json')

        for key, items in combobox_values.items():
            num_key += 1
            num_item = 1

            retorno.append(f'{num_key} - {key}')

            for i in items:
                retorno.append(f'    {num_key}.{num_item} - {i}')
                num_item += 1
        
        return retorno
    
    def alert(self):
        Label(self.container_center, text='Os campos "tipo de atendimento" e "telefone" são obrigatórios!', fg='red', font=('Segoe UI', 9, 'bold')).place(relx=0.05, rely=0.1)


    def fbutton_sincronizar(self):
        scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]

        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.__path__ + "/wpp/files/credentials.json", scopes) #acessa o arquivo json com credenciais da planilha
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread

        # planilha e guia
        ss = file.open("CONTROLE DE CHAMADOS E ATENDIMENTOS") #open sheet
        guiaCS = ss.get_worksheet_by_id(1396832583)

        row = guiaCS.row_count + 1
        for i in self.dados_atendimentos:
            dados = self.dados_atendimentos[i]
            
            i = int(i)
            row += i
            colum = 1
            guiaCS.add_rows(1)
            
            for dado in dados:
                guiaCS.update_cell(row, colum, dado)
                
                colum += 1




    def fbutton_contabilizar(self, event=None):
        tipo_atendimento = self.tipo_atendimento.get()
        telefone = self.telefone.get()
        descricao = self.descricao.get()
        

        if tipo_atendimento == '' or telefone == '':
            self.alert()
        
        else:
            self.dados_atendimentos = Json.getJson(self.fileName)

            if self.dados_atendimentos == None:
                self.dados_atendimentos = {}

            key = str(len(self.dados_atendimentos))
            self.dados_atendimentos[key] = [ self.user, tipo_atendimento, telefone, descricao]

            Json.setJson(self.dados_atendimentos, self.fileName)