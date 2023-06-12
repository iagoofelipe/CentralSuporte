import pyautogui as ag
import sys

while True:
    inp = ag.prompt('Temp: ')
    
    with open('Temp.txt', 'w') as f:
        if inp != '0':
            f.write(inp)
            continue
        
        break

# from multiprocessing import Process
# from functools import partial
# import tkinter as tk    ## Python 3.x

# class ProgressBar():
#     def __init__(self, root):
#         self.root=root
#         self.root.geometry("75x50+900+100")
#         self.ctr=1

#     def counter(self):
#         """ a separate process in a separate GUI
#         """
#         self.top_count=tk.Toplevel(self.root)
#         self.top_count.geometry("75x50+750+50")
#         self.label_ctr = tk.IntVar()
#         self.label_ctr.set(self.ctr)
#         label = tk.Label(self.top_count, textvariable=self.label_ctr)
#         label.pack()
#         self.change_counter()

#     def change_counter(self):
#         self.ctr += 1
#         self.label_ctr.set(self.ctr)
#         self.top_count.after(1000, self.change_counter)


# def stop_process(process_id, PB):
#     process_id.terminate()
#     PB.top_count.destroy()  ## destroy Toplevel to stop "after"

#     ## shut down Tkinter
#     ##root.quit()

# root = tk.Tk()

# PB=ProgressBar(root)
# pr1=Process(target=PB.counter(), args=())
# pr1.start()

# tk.Button(root, text="Exit", bg="orange",
#           command=partial(stop_process, pr1, PB)).pack()
# root.mainloop()