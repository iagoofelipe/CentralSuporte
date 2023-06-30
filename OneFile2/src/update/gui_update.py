import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
from my_tools import File, Registros as reg
from tkinter import font
import os

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


class Update:
    def __init__(self):
        self.root = tk.Tk()
        self.__path__ = reg.get(nome='__path__')
        self.background_color = 'lightgray'

        self.__geometry(300,330)
        self.__font()
        self.root.iconbitmap(self.__path__ + r'icon.ico') # icone da janela
        self.root.title('Central Suporte')
        self.root.resizable(False, False) # responsividade
        self.root.configure(background=self.background_color)
        self.container = tk.Frame(self.root)

        self.container.place(relheight=0.85, relwidth=1)
        self.destroy()

        self.gif()

    def __geometry(self, width, height):
        """ configurando tamanho e centralização da janela """

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        self.root.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))


    def __font(self):
        """ configurando elementos de fonte """

        self.defaultFont = font.nametofont("TkDefaultFont") 
        self.defaultFont.configure(family="Bahnschrift SemiBold Condensed", size=13) 
        self.font_name = self.defaultFont.actual()['family']

    
    def gif(self):
        # carregando gif
        self.lbl = ImageLabel(self.container)
        self.lbl.pack(side='top')
        self.lbl.load(r'C:\Users\IAGO\Desktop\gif\gato_dancando.gif')
        
        self.mensagem = tk.Label(self.root, text='atualização em andamento...\n', background=self.background_color)
        self.mensagem.pack(side='bottom')



    def final(self):
        self.lbl.load(r'C:\Users\IAGO\Desktop\gif\finalizado.jpeg')
        os.remove(f'{self.__path__}end.txt')
        self.mensagem['text'] = 'atualização finalizada com êxito!\nAbra o programa novamente para prosseguir...'


    def loop(self):
        self.root.mainloop()

    def destroy(self):
        file = File.getFile(f'{self.__path__}end.txt')

        if file == ['True']:
            self.final()

        self.root.after(1000, self.destroy)


# if __name__ == '__main__':
#     update = Update()
#     update.loop()