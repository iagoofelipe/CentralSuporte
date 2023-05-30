from _all.Geral import isFile

def verificacao_inicial(m_class):
    """ verificando arquivos necessários """
    result = []

    for arquivo in m_class.arquivos_necessarios:
        fileName = f'{m_class.diretorio_padrao}\\{arquivo}'
        
        # caso o arquivo não exista
        if not isFile(fileName):
            result.append(arquivo)

    return result if result != [] else None