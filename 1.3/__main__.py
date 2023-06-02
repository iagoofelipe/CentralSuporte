from _all.diretorio import diretorio
from GUI.GUI import Application
import sys

class CentralSuporte:
    """ objeto com verificações iniciais, processos e métodos necessários """

    def __init__(self):
        self.diretorio = diretorio
        self.agrv = sys.argv[1:]

if __name__ == "__main__":
    obj = CentralSuporte()
    app = Application(obj)
    
    app.root.mainloop()