from tkinter import *

def bind_verificar(self, event):
    """ bind utilizada para marcar apenas um checkbox por vez """
    
    self.from_bitrix.set(False)
    self.from_local.set(False)
    self.from_manualmente.set(False)

    try:
        self.button_adicionar.place_forget()
        self.entry_manualmente.place_forget()
    except AttributeError:
        pass


def bind_manualmente(self, event):
    self.entry_manualmente = Entry(self.container_center)
    self.button_adicionar = Button(self.container_center, text='adicionar', font=('Calibri', 9, 'normal'), command=self.fbutton_adicionar)
    
    self.button_adicionar.place(relx=0.35, rely=0.49)
    self.entry_manualmente.place(relx=0.1, rely=0.5, relwidth=0.2)
    self.dados = []