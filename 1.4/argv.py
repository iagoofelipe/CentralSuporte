from wpp import argv as wpp

class Agrv:
    """ utilizada para parâmetros posicionais """

    def __init__(self, __path__ : str, argv : list):
        self.__path__ = __path__
        self.argv = argv
        
        self.exe()


    def exe(self):
        # if 'wpp' in self.argv:
        #     wpp = Wpp(self.obj)

        #     wpp.exe()
        
        # else:
        #     print(self.obj.__path__)


        match self.argv[0]:

            case 'wpp':
                wpp(self.__path__, self.argv[1:])