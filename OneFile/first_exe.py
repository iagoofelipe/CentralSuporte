import os, sys
from tools import Json, adm

__path__ = sys.path[0]
fileName = __path__ + r'\settings.json'
users = '"IAGO, HEVERTON, SAMUEL, JOAO, PEDRO"'
   
settings = {
    "build-version" : "1.0.0",
    "users" : users.replace('"', '').split(', '),
    "__path__" : __path__ + '\\',
    "atendimentos-files" : __path__ + "\\src\\atendimentos\\files\\"
}
text = f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\CentralSuporte /v'

os.system(f'{text} {"build-version"} /d {settings["build-version"]} /f')
os.system(f'{text} {"users"} /d {users} /f')
os.system(f'{text} {"__path__"} /d {settings["__path__"]} /f')

Json.setJson(settings, fileName)

adm()