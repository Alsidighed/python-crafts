from tkinter import *
from tkinter import filedialog, messagebox

types = (("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))

def new():
    global path # Без этой инструкции чтение из глобальных переменных остается доступным, чего не сказать о записи, которая осуществляется в локальную (?) переменную с этим же именем
    if tryPreventChangesLostReturnCancelled():
        return
    path = None
    text.delete(1.0, END)
    recalculateSign()
def _open():
    global path
    if tryPreventChangesLostReturnCancelled():
        return
    _path = filedialog.askopenfilename(title = "Открытие", filetypes = types)
    if not _path:
        return
    path = _path
    text.delete(1.0, END)
    f = open(path)
    text.insert(1.0, f.read())
    f.close()
    recalculateSign()
def save():
    _save(False)
def saveAs():
    _save(True)
def _save(raiseSaveFileDialog):
    global path
    if not path or raiseSaveFileDialog:
        _path = filedialog.asksaveasfilename(title = "Сохранение", defaultextension = "txt", filetypes = types) # defaultextension не работает, потому сохранение doc.txt в папке, где есть doc, выдаст ложное предупреждение о перезаписи файла
        if not _path: # Путь не был указан, отмена
            return True
        if _path[-4:] != ".txt": # Исправляем неработающий словарный параметр
            _path += ".txt"
        path = _path # Предотвращение сброса пути текущего файла при отмене выбора нового
    f = open(path, mode = "w")
    f.write(getText())
    f.close()
    recalculateSign()
    return False
def _exit():
    if tryPreventChangesLostReturnCancelled():
        return
    root.destroy()
def about():
    messagebox.showinfo(title = "О программе", message = "Что-то отдаленно похожее на программу для работы с неформатируемым текстом\r\nPaul Nosarev, 2020")
def tryPreventChangesLostReturnCancelled():
    if sign == hash(getText()): # Изменения сохранены или их сохранение не требуется
        return False
    r = messagebox.askyesnocancel(title = "Сохранение", message = "Сохранить файл " + nz(path, "Untitled") + "?")
    if r == None:
        return True
    if r:
        return _save(False)
def getText():
    return text.get(1.0, END)
def recalculateSign():
    global sign
    sign = hash(getText())
def nz(v, ifNull):
    if not v:
        return ifNull
    return v
def countOf_a_o():
    countOfA, countOfO = 0, 0
    for c in getText():
        if c in ("А", "а"): # Русские заглавная и строчная буквы
            countOfA += 1
        if c in ("О", "о"):
            countOfO += 1
    messagebox.showinfo(title = "Количество букв 'а' и 'о'", message = "А = " + str(countOfA) + "\r\nO = " + str(countOfO))

root = Tk()
mainMenu = Menu(root)
root.config(menu = mainMenu)
root.protocol("WM_DELETE_WINDOW", _exit) # Переопределение обработчика события закрытия окна
fileMenu = Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Новый", command = new)
fileMenu.add_command(label = "Открыть", command = _open)
fileMenu.add_command(label = "Сохранить", command = save)
fileMenu.add_command(label = "Сохранить как", command = saveAs)
fileMenu.add_command(label = "Выход", command = _exit)
countingMenu = Menu(mainMenu, tearoff = 0)
countingMenu.add_command(label = "Количество букв 'a' и 'о'", command = countOf_a_o)
helpMenu = Menu(mainMenu, tearoff = 0)
helpMenu.add_command(label = "О программе", command = about)
mainMenu.add_cascade(label = "Файл", menu = fileMenu)
mainMenu.add_cascade(label = "Счет", menu = countingMenu)
mainMenu.add_cascade(label = "?", menu = helpMenu)
text = Text(width = 120, height = 30)
text.pack(side = LEFT)
scrollBar = Scrollbar(command = text.yview)
scrollBar.pack(side = LEFT, fill = Y)
text.config(yscrollcommand = scrollBar.set)
path = None
sign = hash(getText())
root.mainloop()
