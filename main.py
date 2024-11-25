from gtts import gTTS
from tkinter import *
from tkinter import ttk
import os

class Window:
    def __init__(self) -> None:
        self.mainWindow = Tk()
        self.mainWindow.title('TTS')

        ttk.Label(self.mainWindow, text = 'Enter title: ', font = ('Helvetica, 14')).grid(ipadx = 10, sticky = W)
        self.title = ttk.Entry(self.mainWindow)
        self.title.grid(sticky = W, ipadx = 80)

        ttk.Label(self.mainWindow, text = 'Enter text here: ', font = ('Helvetica, 14')).grid(ipadx = 10)

        self.textFrame = ttk.Frame(self.mainWindow)
        self.textFrame.grid()

        self.scroll = Scrollbar(self.textFrame, orient = VERTICAL)
        self.scroll.pack(side = RIGHT, fill = 'y')
        
        self.txt = Text(self.textFrame, font = ('Helvetica, 14'), yscrollcommand = self.scroll.set)
        self.scroll.config(command = self.txt.yview)
        self.txt.pack()

        self.go = ttk.Button(self.textFrame, text = 'Convert', command = self.convert)
        self.go.pack()

        self.mainWindow.mainloop()

    def convert(self):
        self.playWindow = Toplevel()
        self.playWindow.title('Play')

        self.convertTxt = self.txt.get(1.0, 'end-1c')
        self.language = 'en'

        self.converted = gTTS(text = self.convertTxt, lang = self.language, slow = False)
        self.converted.save(f"{self.title.get()}.mp3")

        ttk.Button(self.playWindow, text = 'Play', command = os.system(f"cvlc {self.title.get()}.mp3")).pack()

        self.playWindow.mainloop()

if __name__ == '__main__':
    Window()
