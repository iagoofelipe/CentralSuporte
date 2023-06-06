import sys
from .._all.File import Json
from __init import __path__

if __name__ == '__main__':
    argv = sys.argv[1:]

    # atualizando gid da planilha
    match argv[0]:
        
        case 'gid':
            dados = Json.getJson(__path__ + r'\wpp\files\sheet_info.json')

            dados['gid'] = argv[1]
            Json.setJson(dados, __path__ + r'\wpp\files\sheet_info.json')