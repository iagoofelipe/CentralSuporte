from CentralSuporte import Application
from tkinter import Label

class Teste(Application):
    def __init__(self, address_icon=None, resizable=(False, False), title='Teste 2'):
        super().__init__(address_icon, resizable, title)

    def testando(self):
        # Label(self.container_center, background='red').pack(anchor='center')
        self.container_center.configure(background='red')



teste = Teste(resizable=(True, True))
teste.testando()
teste.loop()