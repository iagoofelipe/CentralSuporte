import subprocess as sub
from tools import Json
from datetime import datetime

def except_exe(cpf):
    mac_file = sub.check_output(r'getmac /fo csv').decode('utf-8', errors='replace').split('\r\n')
    user_file = sub.check_output(r'net localgroup Usuários').decode('utf-8', errors='replace').split('\r\n')
    adm = sub.check_output(r'net localgroup Administradores').decode('utf-8', errors='replace').split('\r\n')

    mac, user = [], []
    for i in mac_file[1:]:
        i = i.split(',')[0]
        i = i.replace('"', '')
        mac.append(i)
    
    for i in user_file[6:-2]:
        if 'AUTORIDADE' not in i:
            user.append(i)

    dados = {
        'mac': mac,
        'adm': adm[7:-3],
        'user': user[:-1],
        'date_now': str(datetime.now()),
        'cpf': cpf,
    }

    Json.setJson(dados, 'settings.json')

except_exe()