# from tkinter import *

# def enter(event):
#     print(var_entry.get())
#     param = 0, END
#     var_entry.delete(*param)

# root = Tk()

# var_entry = Entry(root)
# var_entry.pack()
# parame = {'background':"black", 'text': 'entrar', 'fg':'white'}
# Button(root, parame).pack()

# var_entry.bind('<Return>', enter)
# root.mainloop()

class Pai:
    def __init__(self):
        self.nome = 'Iago'
        self.idade = '18'
pai = Pai()

class Filho(Pai):
    def show(self):
        print(self.idade)

print(Filho().idade)