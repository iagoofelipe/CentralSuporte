
#---------------------------FILE-----------------------------------

""" 
Funções para manipulação de arquivos

    isFile - verifica se arquivo existe
    getFile - retorna conteúdo de um arquivo como lista
    toFile - armazena os dados em um arquivo
    required - verifica arquivos necessários

    Json - manipulação de arquivos json
        Json.getJson - mesmo que getFile
        Json.setJson - mesmo que toFile

    # getDadosBase - extrai dados da base Gestão (base_gestao.csv)

"""

import os, json, subprocess, sys
import win32com.shell.shell as shell
from os.path import exists
__path__ = os.path.abspath('')

def isFile(fileName, diretorio_padrao=True):
    """ Verifica se arquivo existe. """
    if diretorio_padrao:
        fileName = f'{__path__}\\{fileName}'

    return exists(fileName)


def toFile(fileName: str, dados: list | dict | tuple):
    """ 
    gera arquivo com dados informados, substitui o arquivo caso já exista.

    fileName: file.csv
    dados : list

    """
    fileName = f'{__path__}\\{fileName}'
    with open(fileName, 'w') as arquivo:
        
        if type(dados) == dict:
            
            for chave in dados:
                conteudo = dados[chave]
                arquivo.write(str(chave) + ';')
            
                if type(conteudo) == list:
                    for i in conteudo:
                        arquivo.write(i + ';')
                else:
                        arquivo.write(str(conteudo) + ';')

                arquivo.write('\n')
                    
        elif type(dados) in (list, tuple):
            
            for conteudo in dados:
                arquivo.write(str(conteudo) + '\n')
        
        else:
            arquivo.write(str(dados) + '\n')


def getFile(fileName : str) -> list | None:
    """ lendo arquivos e retornando lista com dados """

    file_type = fileName.split('.')[-1]
        
    if isFile(fileName, diretorio_padrao=False) and file_type in ['txt','csv']:

        with open(fileName, 'r') as arquivo:
            try:
                linhas, result = arquivo.readlines(), []
            
                for i in linhas:
                    i = i.strip('\n')
                    
                    if ';' in i:
                        i = i.split(';')

                    result.append(i)
            
                return result
            
            except UnicodeDecodeError:
                pass

    return None # em caso de exceção UnicodeDecodeError ou else


def delFile(fileName: str, diretorio_padrao=True) -> bool:
    """ remove arquivo/pasta especificada """

    try:
        if diretorio_padrao:
            return not bool(os.remove(__path__ + '\\' + fileName))

        else:
            return not bool(os.remove(fileName))
        
    except FileNotFoundError:
        return False


def appendFile(fileName: str, dados: str | list | tuple) -> bool:
    if type(dados) not in (str, list, tuple):
        return False

    with open(__path__ + '\\' + fileName, 'a') as f:
        if type(dados) == str:
            f.write(dados + '\n')
        
        elif type(dados) in (list, tuple):
            for i in dados:
                f.write(i + ';')
            f.write('\n')


class Json:
    """ manipulando arquivos json """

    def getJson(arq_json):
        try:
            with open(arq_json, 'r', encoding='utf8') as f:
                return json.load(f)
        
        except FileNotFoundError:
            return None
        
    def setJson(dados: dict, fileName):
        with open(fileName, 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))


def encode(name, upper=True) -> str:
    from unicodedata import normalize

    ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")        
    return ascii_name.upper() if upper else ascii_name


def nome(name) -> str:
    """ Remove caractere inicial em branco, caso haja, e retorna decodicidado em upperCase """
    return encode(name.strip())
#------------------------------------------------------------------

#-----------------------------sincronizar-------------------------------------
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui as ag
import gspread

def sincronizar(dados_atendimentos):
    nome_planilha = "Central Suporte"
    gid = 290441748
    # nome_planilha = "teste"
    # gid = 1359927816
    
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(__path__ + r'\files\credentials.json', scopes) #acessa o arquivo json com credenciais da planilha
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
#---------------------------------------------------------------------------
#---------------------------ADM------------------------------------
def adm():
    ASADMIN = 'asadmin'
    
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#------------------------------------------------------------------

KEYNAME =  r'HKEY_LOCAL_MACHINE\SOFTWARE\Certfy'
class Registros:
    """ Dados armazenados no Editor de Registro do Windows """

    def get(nome='all') -> dict:
        """ lendo dados de registro """
        try:
            output = subprocess.check_output(rf'reg query {KEYNAME}').decode(errors='ignore').replace(f'\r\n{KEYNAME}\r\n    ', '').split('\r\n')
        except subprocess.CalledProcessError:
            return None
        
        historico_de_registros = {}

        for linha in output:
            linha = linha.strip().split('    REG_SZ    ') # removendo espaço no início e separando chave de dados
            
            if linha == ['']:
                pass
            else:
                historico_de_registros[linha[0]] = linha[1]
        
        return historico_de_registros if nome == 'all' else historico_de_registros[nome]

    def set(**kwargs) -> None:
        adm_exe = True
        if 'dict' in kwargs:
            kwargs = kwargs['dict']

        for nome, dados in kwargs.items():
            os.system(f'reg add {KEYNAME} /v {nome} /d "{dados}" /f')
            
            if adm_exe:
                adm()
                adm_exe = False
#------------------------------------------------------------------

#---------------------------CPF------------------------------------
""" 
    Manipulação de cpf

    formatar - formatação do cpf para padrão com pontos
    validadar - validação do cpf
"""

import re

def formatarCPF(cpf: str | int) -> str:
    """ retorna string do cpf no padrão 000.000.000-00 """
    cpf = str(cpf)
    
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def validarCPF(cpf: str) -> bool:
    # Verifica a formatação do CPF
    cpf = formatarCPF(cpf)
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

#---------------------------------------------------------------------
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#---------------------------------------------------------------------
#-------------------------------GUI-----------------------------------
from tkinter import *
class App:
    def __init__(self):
        self.root = Tk()

        self.__geometry(300,300)
        self.root.iconbitmap(resource_path('certfy.ico')) # icone da janela
        self.root.resizable(False, False) # responsividade
        self.root.title('Inventário Certfy')

        self.container()
        # ag.alert(resource_path('certfy.ico'))

    def __geometry(self, width, height):
        """ configurando tamanho e centralização da janela """

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        self.root.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))

    def container(self):
        self.entry_cpf = Entry(self.root)
        self.entry_cpf.place(relx=0.5, rely=0.5, relwidth=0.8, anchor=CENTER)
        self.entry_cpf.bind('<Return>', self.fbtn_cpf)

        Label(self.root, text='Digite o CPF do agente de registro:', font=('normal', 12)).place(relx=0.5, rely=0.4, anchor=CENTER)
        Button(self.root, text='OK', command=self.fbtn_cpf).place(relx=0.5, rely=0.6, anchor=CENTER)

    def fbtn_cpf(self, event=None):
        cpf = self.entry_cpf.get()
        
        if validarCPF(cpf):
            self.cpf = cpf
            self.root.destroy()
            return
        
        ag.alert('CPF inválido, digite somente os números!')
