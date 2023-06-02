""" 
Funções para manipulação de arquivos

    isFile - verifica se arquivo existe
    getFile - retorna conteúdo de um arquivo como lista
    toFile - armazena os dados em um arquivo
    required - verifica arquivos necessários

    Json - manipulação de arquivos json
        Json.getJson - mesmo que getFile
        Json.setJson - mesmo que toFile

"""

import json
import pyautogui as ag
from os.path import exists

from __init import __path__

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


def required(arquivos: list, caminho: str):
    """ Gera alerta e retorna True caso faltem arquivos """
    for f in arquivos:
        fileName = caminho + '\\' + f
        if not isFile(fileName, False):
            ag.alert(f'Arquivo "{f}" necessário não encontrado!\n\nLocal do arquivo:\n{caminho}')
            return True
        
    return False


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
