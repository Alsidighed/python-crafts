from datetime import *
from urllib.request import *
from re import *

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if self.title == "Программирование":
            self.price *= 2
    def __str__(self):
        return f"\"{self.title}\", {self.author}, {self.pages} страниц, {self.price} рублей, {self.pricePerPage()} рублей на страницу"
    def pricePerPage(self):
        return self.price / self.pages
class Good:
    rate = 0
    day = datetime.today().day
    def __init__(self, name, price, prodYear):
        self.name = name
        self.price = price
        if (prodYear == 2020):
            self.price *= 1.2
        self.prodYear = prodYear
    def __str__(self):
        return f"\"{self.name}\", {self.price} рублей / {self.inEuros()} евро, выпущен в {self.prodYear}, {self.yearsSinceProduction()} лет прошло"
    @staticmethod
    def adjustRate():
        if Good.rate == 0 or Good.day != datetime.today().day:
            Good.day = datetime.today().day
            Good.rate = float(findall("<Value>([^<]+)</Value>", findall("<Valute ID=\"R01239\">(.*)</Valute>", urlopen("http://www.cbr.ru/scripts/XML_daily.asp").read().decode("cp1251"))[0])[0].replace(",", "."))
    def yearsSinceProduction(self):
        return datetime.today().year - self.prodYear
    def inEuros(self):
        Good.adjustRate()
        return self.price / Good.rate
class Matrix:
    def __init__(self, height, width, *args):
        self.height = height
        self.width = width
        self.raw = args
    def __iter__(self):
        return self.raw.__iter__()
    def __mul__(self, n): # умножение на число
        return Matrix(self.height, self.width, *[i * n for i in self])
    @staticmethod
    def digits(num):
        i = 0
        while num != 0:
            num //= 10
            i += 1
        return i
    def __str__(self):
        pad = max([Matrix.digits(i) for i in self])
        return "\n".join([" ".join([str(self.raw[j + i * self.width]).rjust(pad) for j in range(self.width)]) for i in range(self.height)])
print(Book("Сельские почтальоны в Греции и номера штемпелей гашения", "Дерек Виллан", 218, 750))
print(Book("Программирование", "Алена Епифанова", 954, 2900))
print(Good("Семипоплавковый ареометр", 350, 2014))
print(Good("Intel Xeon W-2135", 69790, 2020))
m = Matrix(2, 3, 1, 2, 3, 4, 5, 6)
print(m)
print(m * 2)