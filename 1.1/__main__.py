# instâncias
from _init import Arguments, Verification, diretorio

# from bioac.main import _bioac
from saf.main import saf
from bitrix.main import bitrix
from wpp.main import wpp

from _all.ajuda import _ajuda


class CentralSuporte:
    """ objeto com verificações iniciais, processos e métodos necessários """
    def __init__(self):

        self.arguments = Arguments()
        self.comando = self.arguments.comando.upper()
        self.parametros = self.arguments.parametros

        self.result_verification = Verification().result
        self.diretorio = diretorio
        
        self.main_solicitada = __class__._main_solicitada(self)


    def _main_solicitada(self):
        
        funcs = {
            # 'BIOAC': _bioac,
            'SAF': saf,
            'BITRIX': bitrix,
            'WPP': wpp,
        }

        try:
            return funcs[self.comando]
        
        except KeyError:
            return _ajuda



if __name__ == '__main__':
    obj = CentralSuporte()

    # caso falte algum arquivo obrigatório
    for fileName in obj.result_verification:
        
        if not obj.result_verification[fileName]:
            exit(f'\nArquivo "{fileName}" não encontrado!')
        
    # chamando função a partir do comando passado
    obj_main_solicitada = obj.main_solicitada(obj)

    

