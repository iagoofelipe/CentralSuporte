# módulos python
import os, datetime as dt
import pyautogui as ag

# módulos locais
from _all.Geral import parameters, isFile, getFile, toFile
from bitrix.web import _WebBitrix

# arquivos_de_parametros = {key: (arquivo_para_armazenamento, div)}
arquivos_de_parametros = {

    '/s': ('saf/_files/saf_cpf.txt', 17),
    '/b': ('saf/_files/bioac_cadastrar_cpf.txt', 13)

}

# utilizar a função como comando e a classe como parâmetro para os comandos (saf | bioac)
class Bitrix:

    def __init__(self, parametros: str, diretorio: str):
        self.parametros_aceitos = parameters(parametros, arquivos_de_parametros.keys())
        self.diretorio = diretorio


    def getDados(self, enforce=False):
        """ extraindo dados e acessando a página web para atualização dos dados, caso necessário
        \nenforce = False ::utilizado para comandos que utilizam bitrix como parâmetro, força a extração
           """
        para_seguir, dados, para_consultar = self.parametros_aceitos, {}, {}


        for parametro in para_seguir: # executando apenas os parâmetros passados que são válidos
            nome_arquivo, div = arquivos_de_parametros[parametro]
            se_criar = True

            if isFile(nome_arquivo) and not enforce:
                file_time = dt.datetime.fromtimestamp(os.path.getmtime(self.diretorio + nome_arquivo)).strftime("%d/%m/%Y, %H:%M")
    
                resposta = ag.confirm(
                    f'''Histórico de consulta bitrix localizado!\n\nÚltima atualização do arquivo: {file_time}\nPosição de arquivo: {nome_arquivo}\n\nDeseja realizar uma nova consulta?''',
                    buttons=['Sim', 'Não']
                    )
                
                se_criar = True if resposta == 'Sim' else False


            if se_criar: # caso precise realizar uma nova consulta (se o arquivo não existir, será feita uma nova consulta automaticamente)
                para_consultar[parametro] = (nome_arquivo, div)

            else:# lendo arquivo existente
                dados[parametro] = getFile(nome_arquivo)


        if para_consultar != {}:
            web = _WebBitrix()
            web.webOpen()

            for parametro in para_consultar:
                nome_arquivo, div = para_consultar[parametro]

                cpfs = web.getValues(div)
                dados[parametro] = cpfs
                
                toFile(nome_arquivo, cpfs)
            
            web.webClose() 

        self.dados = dados
        return dados


def bitrix(obj):
    parametros, diretorio = obj.parametros, obj.diretorio
    obj_bitrix = Bitrix(parametros, diretorio)

    return obj_bitrix.getDados()