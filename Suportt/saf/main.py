h = """ 
main principal SAF, realiza processos de verificação e cadastramento

required : .saf.GUI
requested : sub_master(__path__) <object>

"""

# módulos Python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# módulos locais
from ..__init import required, __path__

class Saf:
    def __init__(self):
        self.__path__ = __path__
        self.dir_arq_necessarios = self.__path__ + r'\files'

        self.arquivos_necessarios = ['nomes.csv.gz', 'base_gestao.csv']

        self.error = required(self.arquivos_necessarios, self.dir_arq_necessarios)

    def __webOpen(self) -> None:
        """ Acessando a página SAF """
        
        servico = Service(ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=servico)
        
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


    def __webClose(self) -> None:
        self.__driver.close()
    
    def verificar(self, dados) -> dict:
        """ verificando cpf's cadastrados em SAF """
        self.__webOpen()
        resultado = {}

        for cpf in dados:
            self.__driver.find_element(By.ID,'j_idt54:cpf').send_keys(Keys.HOME + cpf + Keys.RETURN) # teclado
            self.__driver.find_element(By.ID, 'j_idt54:j_idt101').click(); sleep(1)

            consulta = self.__driver.find_element(By.XPATH, '//*[@id="j_idt106:tabelaUsuarios_data"]/tr/td').get_attribute('outerHTML'); sleep(1)

            resultado[cpf] = False if consulta == '<td colspan="5">A pesquisa não obteve resultados</td>' else True

            self.__driver.find_element(By.CSS_SELECTOR,'#j_idt54\:j_idt103 > span').click(); sleep(1)

        self.resultado_verificacao = resultado
        self.__webClose()

    