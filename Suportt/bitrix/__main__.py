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
from ..__init import toFile


if __name__ == '__main__':
    argvs = sys.argv[1:]
    print(h) if argvs == [] else None

    for i in argvs:
        match i:
            case '-f':
                valor = 17 if argvs[argvs.index(i) + 1] == 'saf' else None
                fileName = 'saf/files/cpfs_para_verificar_saf.csv'
                
                if valor != None:
                    bitrix = Bitrix()
                    dados = bitrix.getValues(valor)
                    toFile(fileName, dados)

            case '-h':
                print(h)

            case '-h_class':
                print(h_class)
            