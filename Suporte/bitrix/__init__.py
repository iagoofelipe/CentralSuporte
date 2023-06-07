h = """ 
required : .saf.GUI
requested : ._all.FIle.GetDadosBase <class>
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import pyautogui as ag

from ..__init import GetDadosBase


class Bitrix:
    
    def __webOpen(self, user='61996303687', password='Iago.387954'):
        """ Abertura da conexão """
        self.servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.servico)

        self.driver.get('https://certfy.bitrix24.com.br/crm/deal/kanban/category/3/')
        self.driver.find_element(By.ID,'login').send_keys(user + Keys.RETURN)
        self.driver.find_element(By.CLASS_NAME, 'b24-network-auth-form-btn').click()

        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password + Keys.RETURN)
        self.driver.find_element(By.CSS_SELECTOR, '#authorize-layout > div > div.b24-network-auth-slider > div > form > div > div.b24-network-auth-form-btn-block > button.ui-btn.ui-btn-md.ui-btn-success.ui-btn-round.b24-network-auth-form-btn').click()


    def __webClose(self):
        """ Fechamento da conexão """
        self.driver.close()


    def getValues(self, div) -> list:
        """ captando dados do bitrix, a partir da div (coluna) informada """
        
        self.__webOpen()

        ag.alert('\nNa coluna deseja, desça a página para que a mesma seja carregada por completo. Pressione para continuar...')
        coluna_bitrix = self.driver.find_element(By.XPATH,f'//*[@id="crm_kanban"]/div/div/div[8]/div[{div}]').get_attribute('outerHTML')

        coluna_bitrix = coluna_bitrix.split('\n')
        nomes, cpfs, dados_tratar = [], [], []

        try:
            for linha in coluna_bitrix:
                nome = linha.split('bx-tooltip-classname="crm_balloon_contact">')
                dados_tratar.append(nome)
        except:
            pass

        # pegando nome
        for nome in dados_tratar:
            try:
                nomes.append(nome[1].split('</a>')[0])
            except:
                pass

        # pegando cpf
        for cpf in dados_tratar:
            try:
                cpf = cpf[0].split(' - <span>')[1].split('</span>')[0]
                if len(cpf) == 11:
                    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

                cpfs.append(cpf)
            except:
                pass

        # caso a quantidade de cpfs seja menor que a quantidade de nomes (cpf fora do padrão)
        if len(nomes) > len(cpfs):
            dados_base = GetDadosBase().get()
            
            for nome in nomes:
                for cpf in dados_base:
                    nome_base, _ = dados_base[cpf]

                    if nome == nome_base and cpf not in cpfs:
                        cpfs.append(cpf)

        self.__webClose()
        return cpfs