from os.path import exists
import subprocess
import json
import pyautogui as ag
import re

from _all.diretorio import diretorio

def encode(name, upper=True) -> str:
        from unicodedata import normalize

        ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")        
        return ascii_name.upper() if upper else ascii_name


def nome(name) -> str:
        """ Remove caractere inicial em branco, caso haja, e retorna decodicidado em upperCase """
        return encode(name.strip())


def isFile(fileName, diretorio_padrao=True):
    """ Verifica se arquivo existe. """
    
    if diretorio_padrao:
        fileName = f'{diretorio}\\{fileName}'

    return exists(fileName)


def toFile(fileName: str, dados: list | dict | tuple):
    """ 
    gera arquivo com dados informados, substitui o arquivo caso já exista.

    fileName: file.csv
    dados : list

    """
    fileName = f'{diretorio}\\{fileName}'

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
    fileName = f'{diretorio}\\{fileName}' if diretorio_padrao else fileName
        
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


def parameters(entrada: str, validos: list) -> list:
    """ retorna lista com parametros aceitos, reservado para classes """
    retorno = []

    for valido in validos:
        if valido in entrada:
            retorno.append(valido)

    return retorno


def toDict(keys: list, values: list) -> dict | None:
    """ retorna dicionário e caso de duplicidade, ou None em caso de KeyError  """
    retorno, duplicidade_de_chaves = {}, False
    
    if len(keys) != len(values):
        return None


    for i in range(len(keys)):
        if keys[i] in retorno:
            duplicidade_de_chaves = True
        
        retorno[keys[i]] = values[i]
    
    return retorno, duplicidade_de_chaves



def getDadosBase() -> dict:
    """ pegando informações necessárias (cpf, nome, email) da base """
    dados_base = {}

    with open(diretorio + '/_all/_files/base_gestao.csv') as arquivo:
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

            _nome = nome(_nome)
            email = encode(email, upper=False)

            dados_base[cpf] = [_nome, email]

    return dados_base


class Registros:
    """ Dados armazenados no Editor de Registro do Windows """

    def __init__(self):
        self.diretorio = r'HKEY_LOCAL_MACHINE\SOFTWARE\CentralSuporte'
        self.registros = {}

        __class__.getReg(self)

    def getReg(self) -> dict:
        """ lendo dados de registro """
        output = subprocess.check_output(rf'reg query {self.diretorio}').decode(errors='ignore').replace(f'\r\n{self.diretorio}\r\n    ', '').split('\r\n')

        for linha in output:
            linha = linha.strip().split('    REG_SZ    ') # removendo espaço no início e separando chave de dados
            
            if linha == ['']:
                pass
            else:
                self.registros[linha[0]] = linha[1]

    def setReg(self) -> None:
        pass


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


def arquivos_necessarios(arquivos: list, caminho: str):
    """ Gera alerta e FileNotFoundError caso faltem arquivos """
    for f in arquivos:
        fileName = caminho + '\\' + f
        if not isFile(fileName, False):
            ag.alert(f'Arquivo "{f}" necessário não encontrado!\n\nLocal do arquivo:\n{caminho}')
            return True
        
    return False
    
def format_cpf(cpf: str | int) -> str:
    """ retorna string do cpf no padrão 000.000.000-00 """
    cpf = str(cpf)
    
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def validador_cpf(cpf: str) -> bool:

    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.

    Parâmetros:
        cpf (str): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> validate('529.982.247-25')
    True
    >>> validate('52998224725')
    False
    >>> validate('111.111.111-11')
    False
    """

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