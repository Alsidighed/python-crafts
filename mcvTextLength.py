from tkinter import *

root = Tk()
root.title("16 вариант")
text = StringVar()
text.trace("w", lambda *args: textLen.set(len(text.get())))
textLen = IntVar()
Entry(root, textvariable = text).grid(row = 0, column = 0)
Label(root, text = "Длина текста:").grid(row = 0, column = 1)
Label(root, textvariable = textLen).grid(row = 0, column = 2)
root.mainloop()