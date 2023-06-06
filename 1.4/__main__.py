import sys
from argv import Agrv
from GUI import Application

__version__ = '1.0.4'
__path__ = sys.path[0]
argv = sys.argv[1:]

class CentralSuporte:
    """ objeto com verificações iniciais, processos e métodos necessários """

    def __init__(self):
        self.__path__ = __path__
        self.users = ['IAGO','HEVERTON', 'PEDRO', 'SAMUEL', 'JOAO']

if __name__ == "__main__":

    if argv == []:
        obj = CentralSuporte()
        app = Application(obj)

        app.root.mainloop()
    
    else:
        Agrv(__path__, argv)