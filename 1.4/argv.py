from wpp import Wpp

class Agrv:
    """ utilizada para parâmetros posicionais """

    def __init__(self, obj: object):
        self.obj = obj
        self.argv = obj.argv
        
        self.exe()


    def exe(self):
        if 'wpp' in self.argv:
            wpp = Wpp(self.obj)

            wpp.exe()
        
        else:
            print(self.obj.__path__)
        