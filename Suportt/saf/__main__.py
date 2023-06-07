h = """ 
Utilizado para argumentos posicionais.

    py Suporte.saf comando <valores>

        --v
            verificação no sistema SAF SERPRO

        -h
            descrição de parâmetros
        
        -h_class
            descrição da classe

"""

import sys
from .main import Saf, h as h_class
from ..__init import __path__, getFile

if __name__ == '__main__':
    opcoes_json = ['gid_temp', 'gid_relatorio', 'url', 'ss_name']
    
    argvs = sys.argv[1:]
    # start_index = {
    #     '--u' : 0,
    #     '--show' : 0
    #     }

    for i in argvs:
        match i:
            case '--v':
                saf = Saf()
                saf.verificar(getFile('saf/files/cpfs_para_verificar_saf.csv'))


            case '-h':
                print(h)


            case '-h_class':
                print(h_class)
            