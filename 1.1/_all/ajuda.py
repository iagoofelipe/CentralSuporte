from os import system

def _ajuda(obj):
    # texto de ajuda, contendo informações exibidas em help
    diretorio = obj.diretorio

    try:
        with open(diretorio + '/_all/_files/usage.txt','r') as arquivo:
            texto_ajuda = arquivo.readlines()

    except FileNotFoundError:
        texto_ajuda = [r'File "_all\usage.txt" not found!']
    
    system('cls')

    for i in texto_ajuda:
            print(i)