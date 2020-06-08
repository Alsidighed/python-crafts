from tkinter import *

def _exit(e):
    root.destroy()

root = Tk()
var = StringVar()
Label(root, textvariable = var).grid(row = 0, column = 0)
Entry(root, textvariable = var).grid(row = 1, column = 0)
exitBtn = Button(text = "Выход")
exitBtn.bind("<Button-1>", _exit)
exitBtn.grid(row = 2, column = 0)
root.mainloop()
