# módulos pyhon
import sys

# módulos locais
from src.GUI import Application
from tools import Arguments

def bind(env):
    print(env)

if __name__ == "__main__":
    argvs = sys.argv[1:]

    if argvs == []:
        app = Application()
        app.root.bind('<Control-Return>', bind, add='+')
        app.root.mainloop()
    
    else:
        argv = Arguments(argvs)