import sys

__path__ = sys.path[0]
# # print(__path__)
# argv = sys.argv.copy()
# argv.pop(0)

# print(sys.argv)
# print(argv)
# print(__path__)

class App:
    def __init__(self):
        self.argv = sys.argv[1:]
    
    @staticmethod
    def __path__():
        return sys.path[0]

    def __repr__(self) -> str:
        return 'teste'

print(App().argv)