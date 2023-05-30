# interfaces e interações com usário
import PySimpleGUI as sg
import pyautogui as ag

# acesso e api
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep
import webbrowser
import gspread

class Wpp:

    def __init__(self, obj) -> None:
        self.valores = {}
        self.diretorio = obj.diretorio
        self.atendentes = ['IAGO','HEVERTON', 'PEDRO', 'SAMUEL', 'JOAO']


    def setCheckbox(self) -> int:
        """ marca e conta checkboxs de etiquetas """
        count = 0
        
        while True:
            for pos in ag.locateAllOnScreen(self.diretorio + '/wpp/_images/checkbox.png',confidence=0.7):
                left, top, *_ = pos
                ag.click(left + 10, top + 10)
                count += 1

            locate = ag.locateOnScreen(self.diretorio + '/wpp/_images/mensagem-final.png',confidence=0.7)
       
            if locate == None:
                ag.scroll(-700)
                sleep(0.5)

            else:
                break
      
        return count
    
    def setSheet(self) -> None:
        """ Adiciona valores à planilha de controle """
        
        scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]

        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.diretorio + "/_all/_files/credentials.json", scopes) #acessa o arquivo json com credenciais da planilha
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread

        # planilha e guia
        ss = file.open("CONTROLE DE CHAMADOS E ATENDIMENTOS") #open sheet
        guiaTemplates = ss.get_worksheet_by_id(852765518)

        for i in range(len(self.atendentes)):
            """ seguindo a ordem principal, I H P S J L """
        
            valor = self.valores[i]
            colum = i + 1
            guiaTemplates.update_cell(1, colum, valor)



    # def atendentes(self, window, posicao, event):
    #     atendentes = *self.atendentes, ''
            
    #     if event == 'Avançar':
    #         contagem = __class__.setCheckbox(self)
        
    #     else:
    #         contagem = 0
            
    #     window['-NOME-'].update(atendentes[posicao + 1])
    #     window['-NOME_OLD-'].update(atendentes[posicao])
    #     window['-VALOR-'].update(contagem)
    #     self.valores[posicao] = contagem




# def wpp(obj):
#     obj_wpp = Wpp(obj)

#     window = interface()
#     posicao = 0

#     while True:
#         event, values = window.read()
            
#         if event in ['Avançar', 'Em branco']:
#             window.hide()
#             obj_wpp.atendentes(window, posicao, event)
            
#             if posicao == 5:
#                 break
            
#             posicao += 1
#             window.un_hide()

#         if event in (sg.WIN_CLOSED, 'Sair'):
#             break

#     window.close()
#     obj_wpp.setSheet()
#     webbrowser.open('https://docs.google.com/spreadsheets/d/1k5bo0Vv3GTWSaOS6rKoSX79s42BjQGx9hODg2fuIWuA/edit#gid=32507316')

#     return obj_wpp