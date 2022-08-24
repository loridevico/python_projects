from tkinter import *
from tkinter import ttk


def calcular(*args):
    try:
        val = float(pes.get())
        metros.set((0.3048 * val * 10000.0 + 0.5)/10000.0)
    except ValError:
        pass

root = Tk()
root.title("Conversão de Pés para Metros")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky = (N,W,E,S))
mainframe.columnconfigure(0,weight = 1)
mainframe.rowconfigure(0, weight = 1)

pes = StringVar()
metros = StringVar()

pes_entrada = ttk.Entry(mainframe, width = 7, textvariable = pes)
pes_entrada.grid(column = 2, row = 1, sticky = (W,E))

ttk.Label(mainframe, textvariable = metros).grid(column = 2, row = 2, sticky = (W,E))
ttk.Button(mainframe, text = "CALCULAR", command = calcular).grid(column = 1, row = 3, sticky = W)

ttk.Label(mainframe, text = "pés").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "equivale a").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "metros").grid(column = 3, row = 2, sticky = W)

for child in mainframe.winfo_children(): child.grid_configure(padx = 8, pady = 6)

pes_entrada.focus()
root.bind('<Return>', calcular)

root.mainloop()