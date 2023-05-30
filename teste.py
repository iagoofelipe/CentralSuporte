from tkinter import *
master = Tk()

def var_states():
   print("opcao1: %d, opcao2: %d" % (var1.get(), var2.get()))

Label(master, text="Texto:").grid(row=0, sticky=W)
var1 = BooleanVar()
opcao1 = Checkbutton(master, text="opção 1", variable=var1)
opcao1.grid(row=1, sticky=W)

var2 = BooleanVar()
opcao2 = Checkbutton(master, text="opção 2", variable=var2)
opcao2.grid(row=2, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)


def verificar(event):
    
    var1.set(False)
    var2.set(False)

opcao1.bind('<Button-1>',verificar, add='+')
opcao2.bind('<Button-1>',verificar, add='+')
mainloop()