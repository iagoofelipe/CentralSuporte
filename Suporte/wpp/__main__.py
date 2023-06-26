h = """ 
Utilizado para argumentos posicionais.

    py Suporte.wpp comando <valores>

        --u [ gid_temp | gid_relatorio | url | ss_name ] <valor>
            atualizando configurações de planilha

        --show [ gid_temp | gid_relatorio | url | ss_name | json ]
            exibindo dados de planilha
        
        --w
            contagem e remoção de etiquetas (Wpp.exe)

        --c
            contagem e remoção de etiquetas sem sincronização (Wpp.setCheckbox)

        -h
            descrição de parâmetros
        
        -h_class
            descrição da classe

"""

import sys
from .__init import Wpp, h as h_class
from ..__init import __path__, Json


if __name__ == '__main__':
    opcoes_json = ['gid_temp', 'gid_relatorio', 'url', 'ss_name']
    
    argvs = sys.argv[1:]
    start_index = {
        '--u' : 0,
        '--show' : 0
        }

    print(h) if argvs == [] else None

    for i in argvs:
        match i:
            case '--u':
                dados = Json.getJson(__path__ + r'\wpp\files\sheet_info.json')
                index = argvs.index(i, start_index['--u'])

                tipo = argvs[index + 1]
                conteudo = argvs[index + 2]

                if tipo in opcoes_json:
                    dados[tipo] = conteudo
                    Json.setJson(dados, __path__ + r'\wpp\files\sheet_info.json')
                    print(f'{tipo} updated to "{conteudo}"')
                
                start_index['--u'] += index + 1


            case '--show':
                dados = Json.getJson(__path__ + r'\wpp\files\sheet_info.json')
                tipo = argvs[argvs.index(i) + 1]

                if tipo in opcoes_json:
                    print(f'{tipo}={dados[tipo]}')
                
                elif tipo == 'json':
                    print(f'{opcoes_json=}')

            case '--w':
                wpp = Wpp()
                wpp.exe()

            case '--c':
                wpp = Wpp()
                wpp.setCheckbox()

            case '-h':
                print(h)


            case '-h_class':
                print(h_class)
            