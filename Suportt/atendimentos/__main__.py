# módulos Python
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui as ag
import gspread
import sys
import os

# módulos locais
from ..__init import Json, __path__, isFile
from .__init import h as h_class

fileName = __path__ + '/atendimentos/files/atendimentos_local.json'

# sincronizar
def sincronizar(dados_atendimentos):
    nome_planilha = "CONTROLE DE CHAMADOS E ATENDIMENTOS"
    gid = 1396832583

    if not isFile(r'\atendimentos\files\tipos_de_atendimentos.json') or dados_atendimentos == None:
        ag.alert('Nenhum dado a ser sincronizado!')
        return

    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(__path__ + r"\atendimentos\files\credentials.json", scopes) #acessa o arquivo json com credenciais da planilha
    file = gspread.authorize(credentials) # authenticate the JSON key with gspread

    # planilha e guia
    ss = file.open(nome_planilha) #open sheet
    guiaCS = ss.get_worksheet_by_id(gid)
    row = guiaCS.row_count + 1

    guiaCS.add_rows(len(dados_atendimentos))
    for i in dados_atendimentos:
        
        dados = dados_atendimentos[i]
        
        i = int(i) + row
        cell_list = guiaCS.range(i, 1, i, 4)
        num = 0

        for cell in cell_list:
            cell.value = dados[num]
            num += 1

        guiaCS.update_cells(cell_list)

    temp_path = __path__ + r'\Temp'
    temp_file = __path__ + r'\Temp\atendimentos_local.json'
    atend_file = __path__ + r'\atendimentos\files\atendimentos_local.json'

    if not os.path.exists(temp_path):
        os.mkdir(temp_path)

    Json.setJson(Json.getJson(atend_file), temp_file)
    os.remove(atend_file)


h = """ 
Utilizado para argumentos posicionais.

    py Suporte.saf comando <valores>

        -s
            sincronizando dados locais com database

        -h
            descrição de parâmetros
        
        -h_class
            descrição da classe

"""

if __name__ == "__main__":
    argvs = sys.argv[1:]
    argvs = argvs if len(argvs) != 0 else ['']

    match argvs[0]:
        case '-s':
            dados_atendimentos = Json.getJson(fileName)
            sincronizar(dados_atendimentos)

        case '-h_class':
            print(h_class)

        case _:
            print(h)