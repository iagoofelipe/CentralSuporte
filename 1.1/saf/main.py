from _all.Geral import getFile, toFile, parameters
from saf.old.interface import newDados
from bitrix.main import Bitrix

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

import os, datetime as dt
import pyautogui as ag

# arquivos_de_parametros = {parametro: (arquivo_para_armazenamento, div)}
arquivos_de_parametros = {

    '/v': 'saf/_files/saf_cpf.txt',
    '/b': None,
    # '/c': ('saf/_files/bioac_cadastrar_cpf.txt', 13) # em desenvolvimento

}

class Saf:

    def __init__(self, obj) -> None:
        servico = Service(ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=servico)

        self.diretorio = obj.diretorio
        self.parametros_aceitos = parameters(obj.parametros, arquivos_de_parametros.keys())


    def webOpen(self) -> None:
        """ Acessando a página SAF """
        self.__driver.get('https://saf.serpro.gov.br:8443/iti/inicio.jsf')

        try:
            self.__driver.find_element(By.ID, 'details-button').click()
            self.__driver.find_element(By.ID, 'proceed-link').click()
        
        except:
            pass

        self.__driver.find_element(By.CSS_SELECTOR, '#j_idt56\:j_idt58 > span').click() # login

        # Área de verificação e cadastramento
        self.__driver.find_element(By.ID, 'j_idt23:selecionaSistema_label').click() # caixa selecione
        self.__driver.find_element(By.CSS_SELECTOR, '#j_idt23\:selecionaSistema_panel > div.ui-selectonemenu-items-wrapper > ul > li:nth-child(2)').click() ; sleep(1)# administração
        self.__driver.find_element(By.CSS_SELECTOR, '#j_idt36\:j_idt40 > ul > li > a').click() # usuário
        self.__driver.find_element(By.CLASS_NAME, 'ui-menuitem-link').click()
        self.__driver.find_element(By.CSS_SELECTOR, '#j_idt36\:j_idt40 > ul > li > ul > li > a').click()


    def webClose(self) -> None:
        self.__driver.close()
    

    def getDados(self, parametro):
        nome_arquivo = arquivos_de_parametros[parametro]
        dados = getFile(nome_arquivo)
        se_dados_manualmente = True

        if dados != None: # caso o arquivo exista
            file_time = dt.datetime.fromtimestamp(os.path.getmtime(self.diretorio + nome_arquivo)).strftime("%d/%m/%Y, %H:%M")
    
            resposta = ag.confirm(
                f'''Arquivo com cpfs localizado!\n\nÚltima atualização do arquivo: {file_time}\nPosição de arquivo: {nome_arquivo}\n\nDeseja realizar uma nova consulta?''',
                buttons=['Sim', 'Não']
                )
        
            se_dados_manualmente = True if resposta == 'Sim' else False

        if se_dados_manualmente: # em caso de falha na extração de dados ou digitar manualmente os cpfs
            dados = newDados()
            toFile(nome_arquivo, dados)

        self.dados = dados
        return dados

    
    def verificar(self) -> dict:
        """ verificando cpf's cadastrados em SAF """
        resultado = {}

        for cpf in self.dados:
            self.__driver.find_element(By.ID,'j_idt54:cpf').send_keys(cpf + Keys.RETURN) # teclado
            self.__driver.find_element(By.ID, 'j_idt54:j_idt101').click(); sleep(1)

            consulta = self.__driver.find_element(By.XPATH, '//*[@id="j_idt106:tabelaUsuarios_data"]/tr/td').get_attribute('outerHTML'); sleep(1)

            resultado[cpf] = False if consulta == '<td colspan="5">A pesquisa não obteve resultados</td>' else True

            self.__driver.find_element(By.CSS_SELECTOR,'#j_idt54\:j_idt103 > span').click(); sleep(1)

        self.resultado_verificacao = resultado
        return resultado
    
    
def saf(obj):
    obj_saf = Saf(obj)
    parametros_aceitos = obj_saf.parametros_aceitos
    
    if '/b' in parametros_aceitos:
        Bitrix('/s', obj_saf.diretorio).getDados(enforce=True)


    if '/v' in parametros_aceitos:
        obj_saf.getDados('/v')
        
        obj_saf.webOpen()
        
        resultado_verificacao = obj_saf.verificar()
        print(resultado_verificacao)
        toFile('/saf/_files/resultado_verificacao.csv', resultado_verificacao)

        obj_saf.webClose()