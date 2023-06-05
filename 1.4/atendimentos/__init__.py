""" 
required : .GUI (utilizado em .GUI.Menu)
requested : master(
                root, 
                __path__, 
                container_center, 
                button_color, button_clicked_color, 
                user
                ) <object>,
            
            ._all.File(
                Json <class>, 
                isFile <function>
                ) 
"""

# módulos Python
from oauth2client.service_account import ServiceAccountCredentials
from tkinter.ttk import Combobox
from tkinter import *
import pyautogui as ag
import gspread
import os

# módulos locais
from _all.File import Json, isFile

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
        combobox_values = Json.getJson(self.__path__ + r'\atendimentos\files\tipos_de_atendimentos.json')

        for key, items in combobox_values.items():
            num_key += 1
            num_item = 1

            retorno.append(f'{num_key} - {key}')

            for i in items:
                retorno.append(f'--{num_key}.{num_item} {i}')
                num_item += 1
        
        return retorno
    
    def alert(self):
        Label(self.container_center, text='Os campos "tipo de atendimento" e "telefone" são obrigatórios!', fg='red', font=('Segoe UI', 9, 'bold')).place(relx=0.05, rely=0.1)


    def fbutton_sincronizar(self):
        nome_planilha = "CONTROLE DE CHAMADOS E ATENDIMENTOS"
        gid = 1396832583

        if not isFile(r'\atendimentos\files\tipos_de_atendimentos.json') or self.dados_atendimentos == None:
            ag.alert('Nenhum dado a ser sincronizado!')
            return
        # nome_planilha = "teste"
        # gid = 0

        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]

        self.root.withdraw()
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.__path__ + r"\atendimentos\files\credentials.json", scopes) #acessa o arquivo json com credenciais da planilha
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread

        # planilha e guia
        ss = file.open(nome_planilha) #open sheet
        guiaCS = ss.get_worksheet_by_id(gid)
        row = guiaCS.row_count + 1

        guiaCS.add_rows(len(self.dados_atendimentos))
        for i in self.dados_atendimentos:
            
            dados = self.dados_atendimentos[i]
            
            i = int(i) + row
            cell_list = guiaCS.range(i, 1, i, 4)
            num = 0

            for cell in cell_list:
                cell.value = dados[num]
                num += 1

            guiaCS.update_cells(cell_list)

        temp_path = self.__path__ + r'\Temp'
        temp_file = self.__path__ + r'\Temp\atendimentos_local.json'
        atend_file = self.__path__ + r'\atendimentos\files\atendimentos_local.json'

        if not os.path.exists(temp_path):
            os.mkdir(temp_path)

        Json.setJson(Json.getJson(atend_file), temp_file)
        os.remove(atend_file)
        self.root.deiconify()
        self.dados_atendimentos = None


    def fbutton_contabilizar(self, event=None):
        tipo_atendimento = self.tipo_atendimento.get()
        telefone = self.telefone.get()
        descricao = self.descricao.get()

        if tipo_atendimento == '' or telefone == '':
            self.alert()
            return
        
        self.dados_atendimentos = Json.getJson(self.fileName)

        if self.dados_atendimentos == None:
            self.dados_atendimentos = {}

        key = str(len(self.dados_atendimentos))
        self.dados_atendimentos[key] = [ self.user, tipo_atendimento, telefone, descricao]

        Json.setJson(self.dados_atendimentos, self.fileName)

        self.tipo_atendimento.delete(0, END)
        self.telefone.delete(0, END)
        self.descricao.delete(0, END)