h = """ 
Utilizado para extrair dados do bitrix.

    py Suporte.bitrix comando <valores>

        -f [ saf ]
            força a atualização dos dados coletados em bitrix

        -h
            descrição de parâmetros
        
        -h_class
            descrição da classe

"""

import sys
from . import Bitrix, h as h_class


if __name__ == '__main__':
    argvs = sys.argv[1:]

    for i in argvs:
        match i:
            case '-f':
                valor = 17 if argvs[argvs.index(i) + 1] == 'saf' else None
                
                if valor != None:
                    bitrix = Bitrix()
                    bitrix.getValues(valor)

            case '-h':
                print(h)


            case '-h_class':
                print(h_class)
            