# módulos Python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Bioac:

    def __webOpen(self) -> None:
        """ Acessando a página SAF """
        
        servico = Service(ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=servico)
        
        self.__driver.get('https://form.omni.serpro.gov.br/upperScreenForm/2766'); sleep(1)
        self.__driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/div/button').click()
        
    def __webClose(self) -> None:
        self.__driver.close()

    def cadastrar(self, nome, cpf_agr, email):
        cpf = r'03462721143'

        descricao = f'Informo que o mesmo já teve o seu dossiê anexado no sistema SCDS. Aproveito para solicitar a liberação de acesso do AGR mencionado no Bio-AC.\nCPF: {cpf}\nNOME: {nome}\nE-MAIL: {email}'

        self.__webOpen()
        self.__driver.find_element(By.XPATH, '//*[@id="nav-home"]/div[2]/div/input').send_keys(Keys.HOME + '19.860.129000106' + Keys.RETURN)
        self.__driver.find_element(By.XPATH, '//*[@id="nav-home"]/div[1]/div[1]/input').send_keys(Keys.HOME + cpf + Keys.RETURN); sleep(15)

        i = 0
        pressed = False
        while i < 10:
            try:
                self.__driver.find_element(By.XPATH, '//*[@id="root"]/form/form/div[2]/button[1]').click(); sleep(2) # próximo
                pressed = True
                break
            except:
                sleep(1)
                i += 1
        
        if i == 10 and not pressed:
            input('Clique em próximo e pressione para continuar...')

        self.__driver.find_element(By.XPATH, '//*[@id="nav-profile"]/div[1]/div/select/option[5]').click() # assunto
        self.__driver.find_element(By.XPATH, '//*[@id="nav-profile"]/div[4]/div/input').send_keys(nome)
        self.__driver.find_element(By.XPATH, '//*[@id="nav-profile"]/div[5]/div/input').send_keys(cpf_agr)
        self.__driver.find_element(By.XPATH, '//*[@id="nav-profile"]/div[6]/div/input').send_keys(email)
        self.__driver.find_element(By.XPATH, '//*[@id="nav-profile"]/div[7]/div/input').send_keys("AR CERTFY")
        self.__driver.find_element(By.XPATH, '//*[@id="nav-profile"]/div[8]/div/input').send_keys(descricao); sleep(2)

        input()
        self.__driver.find_element(By.XPATH, '//*[@id="root"]/form/form/div[2]/button[1]').click()

        self.__webClose()

bioac = Bioac()

from ..__init import GetDadosBase, formatar

base = GetDadosBase()
dados_base = base.get()

nome, email = dados_base[formatar('00467135223')]
bioac.cadastrar(nome, '00467135223', email)