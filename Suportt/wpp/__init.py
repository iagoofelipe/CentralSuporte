h = """ 
realiza a contagem e sincronização da planilha com novos números

required : .__main__, self.argv
requested : 
    __path__ <str from .__init>,
    users <list from .__init>,
    Json <class from .__init>

"""

# módulos Python
import pyautogui as ag
from time import sleep

from oauth2client.service_account import ServiceAccountCredentials
import webbrowser
import gspread

from ..__init import __path__, users, Json

class Wpp:
    def __init__(self) -> None:
        self.valores = {}
        self.__path__ = __path__
        self.users = users


    def __setCheckbox(self) -> int:
        """ marca e conta checkboxs de etiquetas """
        count = 0
        
        while True:
            for pos in ag.locateAllOnScreen(self.__path__ + '/wpp/images/checkbox.png',confidence=0.7):
                left, top, *_ = pos
                ag.click(left + 10, top + 10)
                count += 1

            locate = ag.locateOnScreen(self.__path__ + '/wpp/images/mensagem-final.png',confidence=0.7)
       
            if locate == None:
                ag.scroll(-700)
                sleep(0.5)
            else:
                break

        return count


    def __setSheet(self) -> None:
        """ Adiciona valores à planilha de controle """
        
        scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]

        json_file = Json.getJson(self.__path__ + r"\wpp\files\sheet_info.json")
        spreadsheet_name = json_file['ss_name']
        gid_temp = int(json_file['gid_temp'])
        self.url = json_file['url'] + json_file['gid_relatorio']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.__path__ + "/wpp/files/credentials.json", scopes) #acessa o arquivo json com credenciais da planilha
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread

        # planilha e guia
        ss = file.open(spreadsheet_name) #open sheet
        guiaTemplates = ss.get_worksheet_by_id(gid_temp)

        for i in range(len(self.users)):
            """ seguindo a ordem principal, I H P S J L """
        
            valor = self.valores[i]
            colum = i + 1
            guiaTemplates.update_cell(1, colum, valor)


    def exe(self):
        posicao = 0

        for atendente in self.users:
            entrada = input(f'{atendente}: ')

            if entrada == '0':
                self.valores[posicao] = 0
            
            else:
                contagem = self.__setCheckbox()
                self.valores[posicao] = contagem
            
            posicao += 1
        
        self.__setSheet()
        webbrowser.open(self.url)