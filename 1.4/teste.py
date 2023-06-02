from _all.File import Json
from oauth2client.service_account import ServiceAccountCredentials
import gspread

fileName = r'C:\Users\IAGO\Desktop\iago\git\CentralSuporte\1.4\atendimentos\files\atendimentos_local.json'
dados_atendimentos = Json.getJson(fileName)


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\IAGO\Desktop\iago\git\CentralSuporte\1.4/wpp/files/credentials.json", scopes) #acessa o arquivo json com credenciais da planilha
file = gspread.authorize(credentials) # authenticate the JSON key with gspread

# planilha e guia
ss = file.open("CONTROLE DE CHAMADOS E ATENDIMENTOS") #open sheet
guiaCS = ss.get_worksheet_by_id(1396832583)

row = guiaCS.row_count + 1

for i in dados_atendimentos:
    dados = dados_atendimentos[i]

    num = 0
    cell_list = guiaCS.range(row, 1, row, 4)
    
    for cell in cell_list:
        cell.value = dados[num]
        num += 1
    
    row += 1
