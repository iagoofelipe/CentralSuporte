# módulos Python
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui as ag
import gspread
import os

# módulos locais
from tools import Json, __path__, isFile

# sincronizar
def sincronizar(dados_atendimentos):
    nome_planilha = "Central Suporte"
    gid = 2116175800
    local_dir = Json.getJson(__path__ + 'settings.json')["atendimentos-files"]
    

    if not isFile(local_dir + 'atendimentos_local.json', diretorio_padrao=False):
        ag.alert('Nenhum dado a ser sincronizado!')
        return

    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(local_dir + 'credentials.json', scopes) #acessa o arquivo json com credenciais da planilha
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread

        # planilha e guia
        ss = file.open(nome_planilha) #open sheet
    except:
        ag.alert('Verifique sua conexão de internet ou horário local!')
        return
    
    guiaCS = ss.get_worksheet_by_id(gid)
    row = guiaCS.row_count + 1

    guiaCS.add_rows(len(dados_atendimentos))
    for i in dados_atendimentos:
        
        dados = dados_atendimentos[i]
        
        i = int(i) + row
        cell_list = guiaCS.range(i, 1, i, len(dados))
        num = 0

        for cell in cell_list:
            cell.value = dados[num]
            num += 1

        guiaCS.update_cells(cell_list)

    temp_path = local_dir + 'Temp'
    temp_file = local_dir + r'Temp\atendimentos_local.json'
    atend_file = local_dir + 'atendimentos_local.json'

    if not os.path.exists(temp_path):
        os.mkdir(temp_path)

    Json.setJson(Json.getJson(atend_file), temp_file)
    os.remove(atend_file)
    ag.alert('Dados sincronizados com êxito!')