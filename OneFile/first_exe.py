import os
from tools import Json, adm, Registros as reg

__path__ = os.path.abspath('')
fileName = __path__ + r'\settings.json'
users = 'IAGO, HEVERTON, SAMUEL, JOAO, PEDRO'
   
settings = {
    "build-version": "1.0.0",
    "users": users,
    "__path__": __path__ + r'\\',
    "files-path": __path__ + r'\files\\',
    "atendimentos-files": __path__ + r"\files\atendimentos\\",
    "dll": {"atendimentos": ["credentials.json", "tipos_de_atendimentos.json"]}
}
    
reg.set(dict=settings)
settings['users'] = users.split(', ')
Json.setJson(settings, fileName)