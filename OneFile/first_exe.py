import os
from tools import Json, adm, Registros as reg

__path__ = os.path.abspath('')
fileName = __path__ + r'\settings.json'
users = 'IAGO, HEVERTON, SAMUEL, JOAO, PEDRO'
   
settings = {
    "build-version" : "1.0.0",
    "users" : users,
    "__path__" : __path__ + '\\',
    "atendimentos-files" : __path__ + "\\src\\atendimentos\\files\\"
}
    
reg.set(dict=settings)
settings['users'] = users.split(', ')
# Json.setJson(settings, fileName)

adm() # para testes, remover ao gerar executável