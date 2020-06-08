from tkinter import *
# Необходимо для использования Combobox
from tkinter import ttk

cursors = ["X_cursor", "arrow", "based_arrow_down", "based_arrow_up", "boat", "bogosity", "bottom_left_corner", "bottom_right_corner", "bottom_side", "bottom_tee", "box_spiral", "center_ptr", "circle", "clock", "coffee_mug", "cross", "cross_reverse", "crosshair", "diamond_cross", "dot", "dotbox", "double_arrow", "draft_large", "draft_small", "draped_box", "exchange", "fleur", "gobbler", "gumby", "hand1", "hand2", "heart", "icon", "iron_cross", "left_ptr", "left_side", "left_tee", "leftbutton", "ll_angle", "lr_angle", "man", "middlebutton", "mouse", "pencil", "pirate", "plus", "question_arrow", "right_ptr", "right_side", "right_tee", "rightbutton", "rtl_logo", "sailboat", "sb_down_arrow", "sb_h_double_arrow", "sb_left_arrow", "sb_right_arrow", "sb_up_arrow", "sb_v_double_arrow", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "top_left_arrow", "top_left_corner", "top_right_corner", "top_side", "top_tee", "trek", "ul_angle", "umbrella", "ur_angle", "watch", "xterm"]
# 97% цветов вырезано по практическим причинам
colors = ["aquamarine", "azure", "bisque", "blue", "brown1", "burlywood1", "chocolate1", "coral", "cyan", "firebrick1", "gainsboro", "gold", "goldenrod", "gray", "green2", "honeydew2", "ivory2", "ivory3", "ivory4", "khaki", "lavender", "magenta2", "maroon", "navy", "orange", "orchid1", "pink", "plum1", "purple", "red", "salmon", "seashell2", "sienna1", "snow", "tan1", "thistle", "tomato", "turquoise", "wheat1", "yellow"]
aligns = ["left", "center", "right"]
reliefs = ["flat", "raised", "sunken", "groove", "ridge"]

"""
    background, bg - цвет фона
    borderwidth, bd - толщина границы в пикселях
    cursor - курсор, заменяющий основной (черточку), при наведении последнего на виджет
    disabledbackground - цвет фона, когда виджет отключен
    disabledforeground - цвет текста, когда виджет отключен
    exportselection - автоматическое копирование выделенного текста в буфер обмена
    foreground, fg - цвет текста
    font - шрифт (family:size:flags)
    highlightbackground - цвет обводки, когда не в фокусе
    highlightcolor - цвет обводки, когда не в фокусе
    highlightthickness - толщина обводки
    insertbackground - цвет мерцающей черты
    insertborderwidth - ширина границы мерцающей черты
    insertofftime - время, в течении которого черта не отображается
    insertontime - время, в течении которого черта отображается
    insertwidth - ширина черты
    justify - выравнивание текста, если он не заполняет виджет полностью
    readonlybackground - цвет фона, когда виджет находится в режиме "только чтение" - текст можно выделить, но нельзя изменить
    relief - стиль объемной границы виджета
    selectbackground - цвет фона выделения
    selectborderwidth - ширина границы фона выделения
    selectforeground - цвет текста выделения
    show - строка, первым символом которой замещаются все символы вводимого в виджет текста
    state - можно ли изменять текст (normal), можно ли скопировать текст (normal, readonly, -disabled)
    takefocus - возможность доступа к виджету через переключения tab'ом
    textvariable - контейнер-хранилище текста виджета
    -validate - события, вызов которых должен инициировать валидацию виджета, а также конфигурация их входных параметров
    -validatecommand - команда валидации
    width - ширина виджета
    -xscrollcommand - команда прокрутки текста по горизонтали. Обычно scrollbar.set
"""

def parseFont(v): # Преобразование строки, описывающей шрифт, в подходящее для tkinter'а представление - кортеж от 1 элемента - (семейство, размер, флаги). Флаги - строка, где отдельные текстовые флаги разделены символов пробела. Доступные флаги: bold - обводка, italic - курсив, underline - подчерк, overstrike - зачерк
    return tuple(v.split(":"))
def timeProjector(v): # Рядовому человеку сложно уловить 1 миллисекунду, потому увеличим разницу до 50 (похоже, все-таки не миллисекунды.)
    return v * 50
def alignProjector(v): # Если LEFT хранил бы за собой объект, эта проекция имела бы смысл
    return {"left" : LEFT, "center" : CENTER, "right" : RIGHT}[v]
def reliefProjector(v): # same
    return {"flat" : FLAT, "raised" : RAISED, "sunken" : SUNKEN, "groove" : GROOVE, "ridge" : RIDGE}[v]
def tryApply(v, e, se, p, f): # Реализует индикацию значений неверного формата. Пытается назначить Entry e свойство p значением функции f от значения контейнера StringVar v. Если при назначении возникает исключение, цвет фона Entry se, содержащей текст из StringVar v, изменяется на красный, если нет, устанавливается на стандартный (белый) - обращает действие возможно возникшей ранее индикации
    t = e[p] # Сохраним текущее значение свойства
    try:
        e[p] = f(v.get())
        se["bg"] = "white" # Обращение индикации
    except:
        e[p] = t # Свойство могло измениться, возвращаем
        se["bg"] = "red"
def f(v): # f(x) = x
    return v
def c(v): # Упаковывает текст v в контейнер, который возвращает для использования в параметре textvariable 
    r = StringVar()
    r.set(v)
    return r
class LambdaEx: # Обертка лямбды, решающая конкретный случай проблем, вызываемых отсутствием изоляции переменных лямбд. Связывает лямбду l с данными для нее, что содержатся в cfgs (конфигурации), ws (виджеты), es (управляемые Entry), _vars (контейнеры Checkbutton и Entry) через побочное действие (присвоение глобальным переменным) до вызова лямбды
    def __init__(self, l): # Конструктор
        self.l = l
        self.id = id(l) # id возвращает идентификатор объекта в системе сборки мусора
    def __call__(self, *args, **kwargs): # le = LambdaEx(l)   le.__call__() <-> le()
        global cfg, w, v, e
        i = self.id
        cfg = cfgs[i] # Конфигурация используется всеми управляющими виджетами, остальное опционально, что проверяется конструкцией (i in %dict%)
        if i in ws:
            w = ws[i]
        if i in _vars:
            v = _vars[i]
        if i in es:
            e = es[i]
        self.l(*args, **kwargs) # Вызов лямбды

root = Tk()  
r = 0 # Текущая строка для размещения в ней управляемого Entry и виджета управления
cfgs, ws, es, _vars = {}, {}, {}, {} # Хранилища данных для неизолированных по умолчанию лямбд, вызываемых с возникновением событий в управляющих виджетах
for t in [ # Конфигурация главного окна. Представляет собой кортеж из двух элементов - первый описывает свойства управляемого Entry, второй - управляющий виджет - его тип, свойства (только для Combobox), свойство управляемого объекта, функция проекции значения управляющего виджета в значение свойства управляемого Entry
({"textvariable" : c("hello")}, ("cb", colors, "background", f)),
({"textvariable" : c("world")}, ("sp", "borderwidth", f)),
({"textvariable" : c("over your mouse here")}, ("cb", cursors, "cursor", f)),
({"state" : "disabled", "textvariable" : c("disabled")}, ("cb", colors, "disabledbackground", f)),
({"state" : "disabled", "textvariable" : c("disabled")}, ("cb", colors, "disabledforeground", f)),
({"textvariable" : c("select me")}, ("c", "exportselection")),
({"textvariable" : c("colorize me")}, ("cb", colors, "foreground", f)),
({"textvariable" : c("some fancy text")}, ("e", "font", parseFont)),
({"highlightthickness" : 3, "textvariable" : c("some text")}, ("cb", colors, "highlightbackground", f)),
({"highlightthickness" : 3, "textvariable" : c("some text")}, ("cb", colors, "highlightcolor", f)),
({"highlightbackground" : "blue", "highlightcolor" : "red"}, ("sp", "highlightthickness", f)),
({}, ("cb", colors, "insertbackground", f)),
({}, ("sp", "insertborderwidth", f)),
({}, ("sp", "insertofftime", timeProjector)),
({}, ("sp", "insertontime", timeProjector)),
({"textvariable" : c("align me")}, ("cb", aligns, "justify", alignProjector)),
({"state" : "readonly", "textvariable" : c("you can't modify me")}, ("cb", colors, "readonlybackground", f)),
({"borderwidth" : 3}, ("cb", reliefs, "relief", reliefProjector)),
({"textvariable" : c("select part of me")}, ("cb", colors, "selectbackground", f)),
({"textvariable" : c("select part of me")}, ("sp", "selectborderwidth", f)),
({"textvariable" : c("select part of me")}, ("cb", colors, "selectforeground", f)),
({"textvariable" : c("some secure info")}, ("e", "show", f)),
({"textvariable" : c("try modify me")}, ("e", "state", f)),
({"textvariable" : c("reachable by tab")}, ("c", "takefocus")),
({"textvariable" : c("probably a very long string which doesn't fit entry in size")}, ("sp", "width", f))]:
    e = Entry(root, **t[0]) # Создание управляемого Entry в окне root, передача словаря свойств в **kwargs
    e.grid(row = r, column = 0) # Размещение в первом столбце текущей строки
    cfg = t[1] # Конфигурация управляющего виджета
    el = cfg[0] # Тип виджета
    if el == "c": # Флажок
        l = lambda: e.config({cfg[1] : v.get()}) # По изменении флажка вызывается лямбда, меняющая свойство cfg[1] управляемого Entry на текущее значение флажка - 0 при не выставленном, 1 в противном случае 
        v = IntVar() # Контейнер, хранящий состояние флажка
        i = id(l)
        _vars[i] = v # Сохранение контейнера
        w = Checkbutton(root, variable = v, offvalue = 0, onvalue = 1)
        ws[i] = w
        w.config(command = LambdaEx(l)) # Связывание события переключения флажка с изолируемой лямбдой, корректно вызывающей лямбду, меняющую свойство cfg[1] на значение контейнера v
    elif el == "cb": # Выпадающий список
        l = lambda event: e.config({cfg[2] : cfg[3](w.get())}) # cfg[3] - функция проекции значения combobox в форму, пригодную для использования tkinter'ом
        w = ttk.Combobox(root, values = cfg[1])
        i = id(l)
        ws[i] = w
        w.bind("<<ComboboxSelected>>", LambdaEx(l)) # Связывание с событием изменения выбранного элемента
    elif el == "e": # Поле
        l = lambda *args: tryApply(v, e, w, cfg[1], cfg[2]) # Попытка выставить полю e свойство cfg[1] значением функции cfg[2] от значения контейнера v, индикация поля, куда вводится текст в v, красным цветом, если функция выбросила исключение или вернула недопустимое значение
        v = StringVar()
        i = id(l)
        _vars[i] = v
        w = Entry(root, textvariable = v)
        ws[i] = w
        v.trace("w", LambdaEx(l)) # Связывание с событием редактирования текста контейнера
    elif el == "sp": # Диапазон
        l = lambda: e.config({cfg[1] : w.get()})
        i = id(l)
        w = Spinbox(root, from_ = 0, to = 100)
        ws[i] = w
        w.config(command = LambdaEx(l))
    es[i] = e # Сохранение управляемого Entry
    cfgs[i] = cfg # Сохранение конфигурации
    w.grid(row = r, column = 1) # Размещение управляющего виджета справа от управляемого
    r += 1 # Переход на следующую строку
root.mainloop()
