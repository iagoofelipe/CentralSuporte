import sys
import os
from _all.File import Json

__path__ = sys.path[0]

if not os.path.exists(__path__):
    os.mkdir(__path__)
    os.system('winget install python')
    os.system('winget install Git.Git')
    os.system(f'git clone "https://github.com/iagoofelipe/CentralSuporte.git" "{__path__}"')

dados = {
    '__path__' : __path__
}

Json.setJson(dados, __path__ + r'\Settings.json')
