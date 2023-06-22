from oauth2client.service_account import ServiceAccountCredentials
import pyautogui as ag
import gspread

def sincronizar(dados_atendimentos, credentials_path):
    nome_planilha = "Central Suporte"
    gid = 290441748
    # nome_planilha = "teste"
    # gid = 1359927816
    
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scopes) #acessa o arquivo json com credenciais da planilha
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread

        # planilha e guia
        ss = file.open(nome_planilha) #open sheet
    except:
        ag.alert('Verifique sua conexão de internet ou horário local!')
        return
    
    guiaCS = ss.get_worksheet_by_id(gid)
    row = guiaCS.row_count + 1

    guiaCS.add_rows(1)
    cell_list = guiaCS.range(row, 1, row, len(dados_atendimentos))
    num = 0

    for cell in cell_list:
        cell.value = str(dados_atendimentos[num])
        num += 1

    guiaCS.update_cells(cell_list)