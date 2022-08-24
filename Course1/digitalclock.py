import tkinter as tk
from tkinter import font
import time
import datetime

#para sair da aplicacao
def quit(*args):        #iteracao no args que permite flexibilidade de valores passados
    root.destroy()      #sai do widget e mainloop


def clock_time():
    time = datetime.datetime.now()
    #time = (time.strftime("%d-%m-%Y %H:%M:%S"))
    time = (time.strftime("%H:%M:%S"))
    txt.set(time)
    
    root.after(100,clock_time)

root = tk.Tk()     #onde os widgets ficam
root.attributes("-fullscreen", False)
root.configure(background = 'black')
root.bind("x", quit)
root.after(1000, clock_time)        #clock comeca

fnt = font.Font(family='Helvetica', size = 60, weight = 'bold')    #especifica fonte
txt = tk.StringVar()       #segura uma string por padrao
#set propriedades do relogio
lbl = tk.Label(root, textvariable = txt, font = fnt, foreground = "white", background = "black")
#func. geometricas para widget
lbl.place(relx=0.5, rely = 0.5, anchor = tk.CENTER)

root.mainloop()