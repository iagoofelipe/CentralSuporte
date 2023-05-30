import tkinter as tk

window = tk.Tk()
window.columnconfigure(2, minsize=100)
window.rowconfigure([0, 2], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=1, column=1)

label2 = tk.Label(text="B")
label2.grid(row=1, column=0)

window.mainloop()