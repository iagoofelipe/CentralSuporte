from typing import Any
import win32com.shell.shell as shell
import os, subprocess, sys

""" 
categorias:
    REG
    ADM
    CPF
    FILE
    POSITIONAL ARGUMENTS
"""

# __path__ = sys.path[0] # para execução direta
# __path__ = Reg().get('path') # após instalação


#---------------------------REG------------------------------------
KEYNAME =  r'HKEY_LOCAL_MACHINE\SOFTWARE\CentralSuporte'
class Registros:
    """ Dados armazenados no Editor de Registro do Windows """

    def get(nome='all') -> dict:
        """ lendo dados de registro """
        output = subprocess.check_output(rf'reg query {KEYNAME}').decode(errors='ignore').replace(f'\r\n{KEYNAME}\r\n    ', '').split('\r\n')
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
try:
    __path__ = Registros.get('__path__')
except:
    pass
#---------------------------ADM------------------------------------
def adm():
    ASADMIN = 'asadmin'
    
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#------------------------------------------------------------------

#---------------------------CPF------------------------------------
""" 
    Manipulação de cpf

    formatar - formatação do cpf para padrão com pontos
    validadar - validação do cpf
"""

import re

def formatar(cpf: str | int) -> str:
    """ retorna string do cpf no padrão 000.000.000-00 """
    cpf = str(cpf)
    
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def validar(cpf: str) -> bool:
    # Verifica a formatação do CPF
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
#------------------------------------------------------------------

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

import json
import pyautogui as ag
from os.path import exists

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


def getFile(fileName : str, diretorio_padrao=True) -> list | None:
    """ lendo arquivos e retornando lista com dados """

    file_type = fileName.split('.')[-1]
    fileName = f'{__path__}\\{fileName}' if diretorio_padrao else fileName
        
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


def required(arquivos: list, caminho: str) -> bool:
    """ Gera alerta e retorna True caso faltem arquivos """
    for f in arquivos:
        fileName = caminho + '\\' + f
        if not isFile(fileName, False):
            ag.alert(f'Arquivo "{f}" necessário não encontrado!\n\nLocal do arquivo:\n{caminho}')
            return True
        
    return False


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
                f.write(i + '\n')


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


class GetDadosBase:
    def get(self) -> dict:
        """ pegando informações necessárias (cpf, nome, email) da base """
        dados_base = {}

        with open(__path__ + '/files/base_gestao.csv') as arquivo:
            try:
                linhas = arquivo.readlines()
            except UnicodeDecodeError:
                print('Converta o arquivo base para csv (separado por vírgulas)')
                from sys import exit
                exit('Saindo')

            for linha in linhas:
                linha = linha.strip('\n')

                _, cpf, _nome, email, *_ = linha.split(';')
                _nome, *_ = _nome.split('-')

                _nome = self.nome(_nome)
                email = self.encode(email, upper=False)

                dados_base[cpf] = [_nome, email]

        return dados_base
    

    def encode(self, name, upper=True) -> str:
        from unicodedata import normalize

        ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")        
        return ascii_name.upper() if upper else ascii_name


    def nome(self, name) -> str:
        """ Remove caractere inicial em branco, caso haja, e retorna decodicidado em upperCase """
        return self.encode(name.strip())
#------------------------------------------------------------------

#---------------------------------POSITIONAL ARGUMENTS---------------------------------
class Arguments:

    def __init__(self, argvs : list):
        self.__path__ = __path__
        self.categoria = argvs[0]
        self.parametros = argvs[1:]


    def executar(self):
        """ Chamativa do correspondente parâmetro """
        from src.atendimentos import argv as atendimentos
        from src.bitrix import argv as bitrix

        func = {'atendimentos': atendimentos, 'bitrix': bitrix}

        try:
            func[self.categoria](self.parametros)
        except KeyError:
            print('texto de ajuda')
#--------------------------------------------------------------------------------------
