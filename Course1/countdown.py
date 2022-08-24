import tkinter as tk
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime

def quit(*args):
    root.destroy()

def cant_wait():
    #pegar tempo ate evento
    timeLeft = endTime - datetime.datetime.now()
    #remover microsegundos
    timeLeft = timeLeft - datetime.timedelta(microseconds = timeLeft.microseconds)

    txt.set(timeLeft)
    root.after(1000,cant_wait)


#mostrar countdown
root = tk.Tk()
root.attributes("-fullscreen", False)
root.configure(background = 'black')
root.bind("x", quit)
root.after(1000, cant_wait)        #countdown comeca

endTime = datetime.datetime(2022,8,19,9,0,0)

fnt = font.Font(family='Helvetica', size = 60, weight = 'bold')    #especifica fonte
txt = tk.StringVar()       #segura uma string por padrao
#set propriedades do relogio
lbl = tk.Label(root, textvariable = txt, font = fnt, foreground = "white", background = "black")
#func. geometricas para widget
lbl.place(relx=0.5, rely = 0.5, anchor = tk.CENTER)

root.mainloop()