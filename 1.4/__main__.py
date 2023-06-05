import sys, argv
from GUI import Application

__version__ = '1.0.4'

class CentralSuporte:
    """ objeto com verificações iniciais, processos e métodos necessários """

    def __init__(self):
        self.__path__ = sys.path[0]
        self.argv = sys.argv[1:]
        self.users = ['IAGO','HEVERTON', 'PEDRO', 'SAMUEL', 'JOAO']

if __name__ == "__main__":
    obj = CentralSuporte()

    if obj.argv == []:
        app = Application(obj)

        app.root.mainloop()
        pass
    
    else:
        argv.Agrv(obj)