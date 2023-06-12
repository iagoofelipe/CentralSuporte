from tkinter import *
text = 'None'

def read(event=None):
    with open('Temp.txt', 'r') as f:
        text = f.readline()
        label['text'] = text
        label.after(1000, read)


root = Tk()

# Button(root, command=read, text='continuar').place(relx=0.5)
label = Label(root, text=text)
label.place(relx=0.5, rely=0.5)
read()


root.mainloop()