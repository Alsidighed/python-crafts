from tkinter import *
from tkinter import messagebox
from hashlib import *

SINGLE, MULTIPLE, MANUAL = 0, 1, 2
QUESTION, TYPE, ANSWERS, HASH_NO_MANUAL = 0, 1, 2, 3
HASH_MANUAL, VALIDATOR = 2, 3

def removeBraces(s):
    return s.strip(" \t\n\r\"")
def removeSpaces(s):
    return "".join([c for c in s if c not in (" ", "\t", "\n", "\r")])
def _hash(s):
    return sha256(s.encode()).hexdigest()
def verify(a, h, t):
    if t == MULTIPLE:
        return _hash("\0".join([str(n) for n in sorted(a)])) == h
    else:
        return _hash(a) == h
def __hash(a):
    if type(a) == type((1, )):
        return _hash("\0".join([str(n) for n in sorted(a)]))
    else:
        return _hash(a)
def c(t):
    s = StringVar()
    s.set(t)
    return s
def prev():
    global current
    save()
    current -= 1
    setup()
def _next():
    global current
    save()
    current += 1
    if current == len(q):
        summary()
    else:
        setup()
def summary():
    global current, summaryLabels, retryBtn
    summaryLabels = []
    unsolved = [p for p in zip(answers, range(len(answers))) if not p[0] or p == -1 or (type(p[0]) == type((0, )) and sum(p[0]) == 0)]
    _continue = True
    if len(unsolved) != 0:
        if len(unsolved) == 1:
            msg = " " + str(unsolved[0][1] + 1) + " остался"
        else:
            msg = "ы " + ", ".join([str(p[1] + 1) for p in unsolved]) + " остались"
        _continue = messagebox.askyesno(title = "Завершение теста", message = "Вопрос" + msg + " без ответа. Продолжить?")
    if not _continue:
        current -= 1
    else:
        prepareAnswers()
        questionLabel.grid_remove()
        clearBody()
        clearButtons()
        correct = 0
        incorrect = []
        for i in range(len(answers)):
            if q[i][TYPE] == MANUAL:
                if verify(answers[i], q[i][HASH_MANUAL], q[i][TYPE]):
                    correct += 1
                else:
                    incorrect.append(i)
            else:
                if verify(answers[i], q[i][HASH_NO_MANUAL], q[i][TYPE]):
                    correct += 1
                else:
                    incorrect.append(i)
        summaryLines = [str(correct) + "/" + str(len(q)), str(correct / len(q) * 100) + "%", "Ваша оценка: " + getGrade(correct, len(q))]
        summaryLastRow = 3
        if incorrect:
            summaryLines.append("Номера неверных ответов: " + ", ".join([str(n + 1) for n in incorrect]))
            summaryLastRow += 1
        c = 0
        for l in summaryLines:
            lbl = Label(root, text = summaryLines[c])
            lbl.grid(row = c, column = 0)
            summaryLabels.append(lbl)
            c += 1
        retryBtn = Button(root, text = "Заново", command = retry)
        retryBtn.grid(row = summaryLastRow, column = 0)
        exitBtn.grid(row = summaryLastRow + 1, column = 0)
        f = open("summary.txt", mode = "w")
        f.write(str(correct) + "/" + str(len(q)) + "\n" + "\n".join([str(i) + iif(i not in incorrect, " верно ", " неверно ") + iif(answers[i], iif(type(answers[i]) == type((0,)), "\n\t" + "\n\t".join(answers[i]), answers[i]), "<Нет ответа>") for i in range(len(q))]))
        f.close()
def iif(v, iftrue, iffalse):
    if v:
        return iftrue
    return iffalse
def retry():
    global current, manualAnswerEntry, manualAnswerVars, singleAnswerVars, multipleAnswersVars, answersLabels, answerButtonBoxes, singleAnswerRadiobuttons, mutipleAnswersCheckbuttons, answers, summaryLabels
    for l in summaryLabels:
        l.grid_remove()
    retryBtn.grid_remove()
    current = 0
    questions = len(q)
    manualAnswerEntry = None
    manualAnswerVars = [StringVar() for i in range(questions)]
    singleAnswerVars = [IntVar() for i in range(questions)]
    multipleAnswersVars, answersLabels, answerButtonBoxes, singleAnswerRadiobuttons, mutipleAnswersCheckbuttons, summaryLabels = [], [], [], [], [], []
    answers = [None for i in range(len(q))]
    questionLabel.grid(sticky = "W", row = 0, column = 1)
    setup()
def getGrade(c, a):
    p = c / a
    if p >= 0.9:
        return "Отлично"
    if p >= 0.7:
        return "Хорошо"
    if p >= 0.55:
        return "Удовлетворительно"
    return "Неудовлетворительно"
def prepareAnswers():
    global answers
    for i in range(len(answers)):
        if type(answers[i]) == type((1,)):
            answers[i] = tuple([q[i][ANSWERS][j] for j in range(len(q[i][ANSWERS])) if answers[i][j]])
    for i in range(len(answers)):
        if type(answers[i]) == type(""):
            answers[i] = q[i][VALIDATOR](answers[i])
    for i in range(len(answers)):
        if type(answers[i]) == type(0) and answers[i] != -1:
            answers[i] = q[i][ANSWERS][answers[i]]
    for i in range(len(answers)):
        if answers[i] == -1:
            answers[i] = ""
def answersNum():
    return len(q[current][ANSWERS])
def setup():
    global multipleAnswersVars, manualAnswerEntry
    if current == 0:
        prevBtn["state"] = "disabled"
    else:
        prevBtn["state"] = "normal"
    if current == len(q) - 1:
        nextBtnText.set("Завершить")
    else:
        nextBtnText.set(">")
    question.set(q[current][QUESTION])
    clearBody()
    t = q[current][TYPE]
    count = answersNum()
    if t != MANUAL:
        if t == MULTIPLE:
             multipleAnswersVars = [IntVar() for i in range(count)]
        for i in range(count):
            answer = Label(root, text = q[current][ANSWERS][i], justify = "left", anchor = "w")
            answer.grid(sticky = "W", row = i + 1, column = 1)
            answersLabels.append(answer)
            if t == MULTIPLE:
                w = Checkbutton(root, variable = multipleAnswersVars[i], offvalue = 0, onvalue = 1)
                c = mutipleAnswersCheckbuttons
            if t == SINGLE:
                singleAnswerVars[current].set(-1)
                w = Radiobutton(root, variable = singleAnswerVars[current], value = i)
                c = singleAnswerRadiobuttons
            w.grid(sticky = "W", row = i + 1, column = 0)
            c.append(w)
    else:
        manualAnswerEntry = Entry(root, textvariable = manualAnswerVars[current])
        manualAnswerEntry.grid(sticky = "W", row = 1, column = 1)
    clearButtons()
    lastRow = count + 1
    prevBtn.grid(sticky = "W", row = lastRow, column = 0)
    nextBtn.grid(sticky = "W", row = lastRow, column = 1)
    exitBtn.grid(sticky = "w", row = lastRow + 1, column = 1)
    trySetAnswers()
def clearBody():
    global answersLabels, singleAnswerRadiobuttons, manualAnswerEntry, mutipleAnswersCheckbuttons
    for l in answersLabels:
        l.grid_remove()
    for cb in mutipleAnswersCheckbuttons:
        cb.grid_remove()
    for rb in singleAnswerRadiobuttons:
        rb.grid_remove()
    if manualAnswerEntry:
        manualAnswerEntry.grid_remove()
    answersLabels, mutipleAnswersCheckbuttons, singleAnswerRadiobuttons = [], [], []
    manualAnswerEntry = None
def clearButtons():
    prevBtn.grid_remove()
    nextBtn.grid_remove()
    exitBtn.grid_remove()
def trySetAnswers():
    if answers[current]:
        t = q[current][TYPE]
        if t == MANUAL:
            manualAnswerVars[current].set(answers[current])
        elif t == SINGLE:
            singleAnswerVars[current].set(answers[current])
        elif t == MULTIPLE:
            for i in range(answersNum()):
                multipleAnswersVars[i].set(answers[current][i])
def save():
    t = q[current][TYPE]
    if t == SINGLE:
        answers[current] = singleAnswerVars[current].get()
    elif t == MULTIPLE:
        answers[current] = tuple(map(lambda v: v.get(), multipleAnswersVars))
    elif t == MANUAL:
        answers[current] = manualAnswerVars[current].get()
    
q = [("Какие из предоставленных типов занимают ровно 2 байт памяти?", MULTIPLE, ("System.UInt16", "byte", "IntPtr", "char", "char*", "short&","long", "ulong*"), "be6a95fc9522821c9c4e15c66ea9e3081d2c2a40ef030744390b5a27db88b02b"), ("Выберите из списка все небезопасные структуры", MULTIPLE, ("struct Point {int x; int y; }", "struct TBStr {char* ptr; long count;}", "struct Person {string name; string surname; int age;}", "struct S<T> where T : IEquatable<T>, struct {}", "struct @unsafe {void* src; void* dst, int sz; EventHandler callback;}"), "24284b938dee8ba938658ac6f573d76eefb0bab2f70c39657e02a3ceb0d0acb2"), ("Каков результат функции F(\"2\")?\nstring F(string s)  {\nSystem.Numerics.BigInteger n = System.Numerics.BigInteger.Parse(s);\nreturn (n * (n *= n * n) * (n *= n) * n * (n *= (n *= n * n) * n) * n).ToString();\n}", MANUAL, "5ee7924f903dfefa9253b5f63147f53433516da9daf01f6e729331dcf31b28c6", removeBraces), ("В каких ситуациях код в блоке finally не выполнится?", MULTIPLE, ("Переполнение стека", "throw new StackOverflowException()", "Environment.FailFast()", "int n = 10 % 0;", "typeof(string).MakePointerType()", "//НЕ ВЫПОЛНЯТЬ!\n[DllImport(\"ntdll.dll\")]\nstatic extern uint RtlAdjustPrivilege(int privilege, bool bEnablePrivilege, bool isThreadPrivilege, out bool previousValue);\n[DllImport(\"ntdll.dll\")]\nstatic extern uint RtlSetProcessIsCritical(bool bNew, out bool pbOld, bool bNeedScb);\n\nRtlAdjustPrivilege(20, true, false, out _);\nRtlSetProcessIsCritical(true, out _, false);\nEnvironment.Exit(0);"), "8734ceffc16d1853989cc6d2edd9446d4a89ba72695f3fb5c8b13cf73c2ccd7d"), ("Получите третий элемент первой строки первого ряда второго массива int[][,,] array, используя null-условную индексацию трехмерного массива", MANUAL, "025fda15d3f1f2964b36741b08ba696e0cdb1b8fc43596642ea59aa10f381c9c", removeSpaces), ("Выберите все базовые типы C#", MULTIPLE, ("Классы", "Делегаты", "Перечисления", "Структуры", "Интерфейсы", "События", "Поля", "Свойства", "Массивы", "Указатели", "Индексаторы", "Обнуляемые типы"), "f745cd3c0180aa4b475c45448adab124a1167a90de37fb0aefb3741a2d8a6371"), ("Какие из типов допустимы для типа возвращаемого значения (unsafe) метода?", MULTIPLE, ("int?", "object?", "Dictionary<void*, int[][][,,,,]>", "float&", "ArgIterator", "byte*****", "Func<Func<Func<Func<int>>>>"), "27cd708e12fe309cc72433ddb33e0bdb8e55222deaffda4021a64742483dbdf6"), ("Выберите класс, осуществляющий двусторонние преобразования примитивов и байт", SINGLE, ("Convert", "BitConverter", "Struct", "Bittable"), "8de74edafa01faa1d80453e3114b3993f15dce2297dec6e68ca86e1531608a21"), ("Выберите опкоды инструкций языка MSIL, которые нельзя получить в программе, используя чистый C#", MULTIPLE, ("tailcall.", "ldind.i4", "initblk", "calli", "ldobj", "break", "constrained", "bgt.un.s", "endfilter", "ckfinite", "jmp", "mkrefany", "ldftn", "unaligned."), "464f37f77ed7ad627b9a6a56d513fe2e35641d03c0f8c24326f79ecb9f44973e"), ("Получите objH левого потомка правого потомка четвертой структуры\nunsafe struct TreeNode\n{\n\tpublic TreeNode* left;\n\tpublic TreeNode* right;\n\tpublic IntPtr objH;\n}\nимея указатель на указатель на начало неуправляемого массива ptr, не используя оператор разыменовывания", MANUAL, "2a1112dd29e41aa916187e3bb294d75b5a9206f805d4891dbc7e2e45d3da74e7", removeSpaces)]
root = Tk()
current = 0
questions = len(q)
manualAnswerEntry = None
manualAnswerVars = [StringVar() for i in range(questions)]
singleAnswerVars = [IntVar() for i in range(questions)]
multipleAnswersVars, answersLabels, answerButtonBoxes, singleAnswerRadiobuttons, mutipleAnswersCheckbuttons, answers, summaryLabels = [], [], [], [], [], [], []
retryBtn = None
answers = [None for i in range(len(q))]
question = StringVar()
questionLabel = Label(root, textvariable = question, anchor = "w")
questionLabel.grid(sticky = "w", row = 0, column = 1)
prevBtn = Button(root, textvariable = c("<"), command = prev)
nextBtnText = c(">")
nextBtn = Button(root, textvariable = nextBtnText, anchor = "w", command = _next)
exitBtn = Button(root, textvariable = c("Выход"), anchor = "w", command = root.destroy)
setup()
root.mainloop()