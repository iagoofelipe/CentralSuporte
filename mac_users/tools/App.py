from tkinter import *
from tools import validarCPF

import pyautogui as ag

class App:
    def __init__(self):
        self.root = Tk()

        self.__geometry(300,300)
        self.root.iconbitmap('certfy.ico') # icone da janela
        self.root.resizable(False, False) # responsividade
        self.root.title('Inventário Certfy')

        self.container()

    def __geometry(self, width, height):
        """ configurando tamanho e centralização da janela """

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        self.root.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))

    def container(self):
        self.entry_cpf = Entry(self.root)
        self.entry_cpf.place(relx=0.5, rely=0.5, relwidth=0.8, anchor=CENTER)
        self.entry_cpf.bind('<Return>', self.fbtn_cpf)

        Label(self.root, text='Digite o CPF do agente de registro:', font=('normal', 12)).place(relx=0.5, rely=0.4, anchor=CENTER)
        Button(self.root, text='OK', command=self.fbtn_cpf).place(relx=0.5, rely=0.6, anchor=CENTER)

    def fbtn_cpf(self, event=None):
        cpf = self.entry_cpf.get()
        
        if validarCPF(cpf):
            self.cpf = cpf
            return
        
        ag.alert('CPF inválido, digite somente os números!')
        # self.entry_cpf.delete(0, END)

        
# if __name__ == '__main__':
#     app = App()
#     app.root.mainloop()