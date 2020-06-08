from tkinter import *
from winsound import *

root = Tk()
Button(root, text = 'Звук!', command = lambda: Beep(2000, 1000)).pack()
Button(root, text = "Выход", command = root.destroy).pack()
root.mainloop()

from tkinter import *

root = Tk()
root.title('Какая кнопка нажата?')
btn = Button(root, text = 'Нажмите любую кнопку мыши')
btn.pack()
Button(root, text = "Выход", command = root.destroy).pack()
btn.bind('<Button-1>', lambda e: print('Вы нажали левую кнопку'))
btn.bind('<Button-3>', lambda e: print('Вы нажали правую кнопку'))
root.mainloop()

from tkinter import *

def left(e):
    lbl["text"] = ('Вы нажали левую кнопку')
def right(e):
    lbl["text"] = ('Вы нажали правую кнопку')

root = Tk()
root.title('Какая кнопка нажата?')
btn = Button(root, text = 'Нажмите любую кнопку мыши')
btn.bind('<Button-1>', left)
btn.bind('<Button-3>', right)
btn.pack()
lbl = Label(root, text = "Пока ничего не нажато")
lbl.pack()
Button(root, text = "Выход", command = root.destroy).pack()
root.mainloop()

from tkinter import *

def new_window(event):
    window = Toplevel(root)
    window.geometry('400x400')
    window.title('Второе окно')
    entry = Entry(window, textvariable = val)
    but2 = Button(window, text='Ok')
    entry.pack()
    but2.pack()

root = Tk()
root.geometry('300x300')
root.title('Основное окно')
lab = Label(root, text = 'Нажми')
lab.pack()
but = Button(root, text = 'Ok')
but.bind('<Button-1>', new_window)
but.pack()
val = StringVar()
entry = Entry(root, textvariable = val)
entry.pack()
Button(root, text = "Выход", command = root.destroy).pack()
root.mainloop()

from tkinter import *

root = Tk()
btn = Button(root, text = 'Нажмите что-нибудь')
btn.bind('<1>', lambda e: print('Вы нажали левую кнопку'))
btn.bind('<2>', lambda e: print('Вы нажали среднюю кнопку'))
btn.bind('<3>', lambda e: print('Вы нажали правую кнопку'))
btn.bind("<B1-Motion>", lambda e: print("Вы нажали левую кнопку и сдвинули курсор"))
btn.bind("<ButtonRelease-1>", lambda e: print("Вы отпустили левую кнопку"))
btn.bind("<Double-Button-1>", lambda e: print("Вы нажали левую кнопку 2 раза"))
btn.bind("<Triple-Button-1>", lambda e: print("Вы нажали левую кнопку 3 раза"))
btn.bind("<Enter>", lambda e: print("Вы навели курсор на кнопку"))
btn.bind("<Leave>", lambda e: print("Вы убрали курсор с кнопки"))
root.bind("<Return>", lambda e: print("Вы нажали enter"))
root.bind('<Key>', lambda e: print('Вы нажали ' + repr(e.char)) if repr(e.char) != "''" else None)
root.bind("<Shift-Up>", lambda e: print("Вы нажали вверх при нажатом shift"))
root.bind("<Configure>", lambda e: print("Размеры виджета изменились"))
btn.pack()
Button(root, text = "Выход", command = root.destroy).pack()
root.mainloop()