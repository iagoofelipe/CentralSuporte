from src.atendimentos.GUI import GUI
from src.atendimentos.main import sincronizar

h = """ 
Sessão Atendimentos da interace principal, utilizado para contabilizar e categorizar
os atendimentos feitos durante o dia.

    py Suporte.saf comando <valores>

        --s
            sincronizando dados locais com database

        -h
            descrição de parâmetros
        
        -h_class
            descrição da classe
"""

def argv(argvs):
    """ Função para ser usada com parâmetros posicionais, utilizado no console de desenvolvedor"""
    from tools import Json, __path__

    local_dir = Json.getJson(__path__ + 'settings.json')['atendimentos-files']
    fileName = local_dir + 'atendimentos_local.json'

    match argvs[0]:
        case '--s':
            dados_atendimentos = Json.getJson(fileName)
            sincronizar(dados_atendimentos)

        case _:
            print(h)


__all__ = [GUI, sincronizar, argv]