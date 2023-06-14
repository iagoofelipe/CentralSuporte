import sys
from tkinter import *

argvs = sys.argv
print(argvs)

root = Tk()
Entry(root).place(relx=.5)
Button(root, text='proximo').place(relx=.5, rely=.2)
root.mainloop()