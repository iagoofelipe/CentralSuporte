import pyautogui as ag
from time import sleep
from ..__init import GetDadosBase, formatar, __path__, getFile, toFile
import pyperclip as pc

cpf_login = '03462721143'
cnpj = '19.860.129000106'
x, y = 0, 0
__path__ += r'\bioac\files\\'

with open(__path__ + 'cpfs_para_cadastrar_bioac.csv', 'r') as f:
    _f = f.readlines()
    cpfs_cadastrar = []

    for i in _f:
        i = i.strip('\n')
        cpfs_cadastrar.append(i)

base = GetDadosBase()
dados_base = base.get()

for cpf in cpfs_cadastrar:
    cpf_sem_formatacao = cpf
    cpf = formatar(cpf)

    nome, email = dados_base[cpf]
    descricao = f'Informo que o mesmo ja teve o seu dossie anexado no sistema SCDS. Aproveito para solicitar a liberacao de acesso do AGR mencionado no Bio-AC.\nCPF: {cpf}\nNOME: {nome}\nE-MAIL: {email}'


    def write(image : str, text : str, time_sleep=0, plus_x=0, plus_y=0):
        global x, y
        x, y = ag.locateCenterOnScreen(__path__ + r'pyautogui\\' + image)
        ag.click(x + plus_x, y + plus_y)
        ag.press('home')
        ag.write(text)
        sleep(time_sleep)

    write('cnpj_login.png', cnpj)
    write('cpf_login.png', cpf_login, 1)

    # contagem = 0
    # while True:
    #     try:
    #         x, y = ag.locateCenterOnScreen(__path__ + 'msg_aguarde.png')
    #         print(contagem)
    #         contagem += 1
    #     except:
    #         break

    sleep(10)
    ag.click(ag.locateCenterOnScreen(__path__ + r'pyautogui\\' + 'proximo.png')); sleep(10)
    ag.click(ag.locateCenterOnScreen(__path__ + r'pyautogui\\' + 'selecione.png')); sleep(2)
    ag.click(ag.locateCenterOnScreen(__path__ + r'pyautogui\\' + '1_3.png')); sleep(2)

    ag.scroll(-1000)
    write('nome.png', nome, 0.5)

    y += 100
    ag.click(x, y)
    ag.press('home')
    ag.write(cpf)

    ag.click(84, 366)
    ag.press('home')
    ag.write(email)

    ag.click(80, 448)
    ag.press('home')
    ag.write('AR CERTFY')

    ag.click(107,530)
    ag.press('home')
    ag.write(descricao); sleep(5)

    ag.click(462,763); sleep(4) # enviar

    inicio = 660,533
    fim = 801,528

    ag.click(inicio)
    ag.keyDown('shift')
    ag.click(fim)
    ag.keyUp('shift')
    ag.hotkey('ctrl', 'c')
    protocolo = pc.paste()

    with open(__path__ + 'cadastrados.csv', 'a') as f:
        f.write(f'{cpf};{nome};{email};{protocolo}\n')
        cpfs_cadastrar.remove(cpf_sem_formatacao)
        toFile(r'\bioac\files\cpfs_para_cadastrar_bioac.csv', cpfs_cadastrar)

    ag.click(411,84); sleep(2)
