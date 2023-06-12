import threading
import os

def inicia_programa(nome_arquivo, argvs):
    os.system('py {} {}'.format(nome_arquivo, argvs))

if __name__ == "__main__":

    arquivos = {
        'teste2.py' : '--v',
        'teste.py' : '-h as helper'
        }

    processos = []
    for arquivo in arquivos:
        argvs = arquivos[arquivo]

        processos.append(threading.Thread(target=inicia_programa, args=(arquivo, argvs)))

    for processo in processos:
        processo.start()