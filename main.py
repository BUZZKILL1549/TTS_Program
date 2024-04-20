from gtts import gTTS
import os
from tkinter import *
from tkinter import ttk

mainWindow = Tk()
mainWindow.geometry()
mainWindow.title('TTS')

ttk.Label(mainWindow, text = 'Enter the title: ', font = ('Helvetica, 14')).grid(ipadx = 10, sticky = W)
title = ttk.Entry(mainWindow)
title.grid(sticky = W, ipadx = 80)

ttk.Label(mainWindow, text = 'Enter your text here: ', font = ('Helvetica, 14')).grid(ipadx = 10)

# Defining the scrollbar, text and button widget

textFrame = ttk.Frame(mainWindow)
textFrame.grid()

scroll = Scrollbar(textFrame, orient='vertical')
scroll.pack(side = RIGHT, fill = 'y')

txt = Text(textFrame, font = ('Helvetica, 14'), yscrollcommand = scroll.set)
scroll.config(command = txt.yview)
txt.pack()

def convert():
    playWindow = Toplevel(mainWindow)
    playWindow.title('Play')

    convertTxt = txt.get(1.0, 'end-1c')
    language = 'en'

    converted = gTTS(text = convertTxt, lang = language, slow = False)
    converted.save(f"{title.get()}.mp3")

    ttk.Button(playWindow, text = 'Play', command = os.system(f"start {title.get()}.mp3")).pack()

go = ttk.Button(textFrame, text = 'Convert', command = convert)
go.pack()

mainWindow.mainloop()