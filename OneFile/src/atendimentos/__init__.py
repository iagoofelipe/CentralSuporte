from src.atendimentos.GUI import GUI
from src.atendimentos.main import sincronizar

h = """ 
Utilizado para argumentos posicionais.

    py Suporte.saf comando <valores>

        -s
            sincronizando dados locais com database

        -h
            descrição de parâmetros
        
        -h_class
            descrição da classe
"""

def argv(argvs):
    """ Função para ser usada com parâmetros posicionais, diretamente do terminal """
    from tools import Json, __path__
    
    local_dir = Json.getJson(__path__ + 'settings.json')['atendimentos-files']
    argvs = argvs if len(argvs) != 0 else ['']
    fileName = local_dir + 'atendimentos_local.json'

    match argvs[0]:
        case '-s':
            dados_atendimentos = Json.getJson(fileName)
            sincronizar(dados_atendimentos)

        # case '-h_class':
        #     print(h_class)

        case _:
            print(h)



__all__ = [GUI, sincronizar, argv]