from tkinter import *
import os
from multiprocessing import Process

class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x700')
        self.__container()
    
    def __container(self):
        self.container = Frame(self.root)
        self.container.grid(sticky=W)

        self.inp = Entry(self.container)
        self.inp.grid(row=3)
        
        Button(self.container, command=self.fb_new_process, text='Próximo').grid(row=4)

    def fb_new_process(self, event=None):
        inp = self.inp.get()
        pr1=Process(target=os.system(f'py {inp}'), args=())
        pr1.start()

        

if __name__ == '__main__':
    app = App()

    app.root.mainloop()