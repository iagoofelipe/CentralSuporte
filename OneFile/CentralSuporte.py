# módulos pyhon
import sys

# módulos locais
from tools import Arguments, Json, isFile, Registros
from src.GUI import Application

def bind(env):
    print(env)

if __name__ == "__main__":
    argvs = sys.argv[1:]

    if argvs == []:
        app = Application()
        app.root.bind('<Control-Return>', bind, add='+')
        app.root.mainloop()
    
    else:
        pass
        # argv = Arguments(__path__, argvs)