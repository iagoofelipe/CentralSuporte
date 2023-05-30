import argparse, pyautogui as ag
import datetime as dt

diretorio = __file__.replace(f'{__name__}.py','')
diretorio_padrao = '/_all/_files'
arquivos_necessarios = ['base_gestao.csv','credentials.json','nomes.csv.gz']


class Arguments:
    """ parâmetros posicionais """

    def __init__(self):
        parser = __class__._constructor()

        self.args = parser.parse_args()
        self.comando = self.args.comando[0].upper()
        self.parametros = self.args.comando[1:]


    def _constructor():
        # parametros posicionais
        parser = argparse.ArgumentParser(prog='Central Suporte',description='Central do Suporte, automatizando processos utilizados no dia a dia', usage='Para uma melhor descrição, utilize file.py help')
        parser.add_argument('comando', action="extend", nargs='+', help='help para melhor descrição')

        return parser
    


class Verification:
    """ verificação inicial de arquivos necessários """

    def __init__(self) -> None:
        self.arquivos_necessarios = arquivos_necessarios
        self.result = __class__.initial(self)


    def initial(self) -> dict:
        from _all.Geral import isFile
        result = {}

        for arquivo in self.arquivos_necessarios:
            
            fileName = f'{diretorio_padrao}\\{arquivo}'
            result[arquivo] = isFile(fileName)
            
        if arquivo == 'base_gestao.csv':
            ag.alert('')


        return result
