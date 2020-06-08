from random import randint as rnd
from functools import reduce
from urllib.request import *
from datetime import *
from re import *

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def __str__(self):
        return f"Длина: {self.height}, ширина: {self.width}, периметр: {(self.height + self.width) * 2}, площадь: {self.height * self.width}"
class Calc:
    def __init__(self, first, second, *args):
        self.first = first
        self.second = second
        self.rest = args
    def nums(self):
        rest = ", ".join([str(i) for i in self.rest])
        return f"a = {self.first}, b = {self.second}, rest = [{rest}]"
    def sumAll(self):
        return "Сумма = " + str(self.first + self.second + sum(self.rest))
    def mulAll(self):
        return "Произведение = " + str(reduce(lambda f, s: f * s, [self.first, self.second, *self.rest]))
    def subAll(self):
        return "Разность = " + str(reduce(lambda f, s: f - s, [self.first, self.second, *self.rest]))
    def div(self):
        if self.second == 0:
            return "a / b = Division by zero"
        return "a / b = " + str(self.first / self.second)
    def pow(self):
        return "a ^ b = " + str(self.first ** self.second)
class CurrencyConverter:
    day = datetime.today().day
    data = {}
    def __init__(self, value):
        self.value = value
        CurrencyConverter.ensureExchangeRatesUpToDate() # initialize exchange rates
    def __getitem__(self, item):
        CurrencyConverter.ensureExchangeRatesUpToDate()
        if item not in CurrencyConverter.data:
            return ""
        return f"{self.value} Российский Рубль = {self.value / CurrencyConverter.data[item][1]} {CurrencyConverter.data[item][0]}"
    def __iter__(self):
        return CurrencyConverter.data.keys().__iter__()
    @staticmethod
    def ensureExchangeRatesUpToDate():
        if not CurrencyConverter.data or len(CurrencyConverter.data.keys()) == 2 or CurrencyConverter.day != datetime.today().day:
            CurrencyConverter.day = datetime.today().day
            try:
                xml = urlopen("http://www.cbr.ru/scripts/XML_daily.asp").read().decode("cp1251")
                l = []
                for w in ("CharCode", "Nominal", "Name", "Value"):
                    l.append(findall(f"<{w}>([^<]+)</{w}>", xml))
                for i in range(len(l[0])):
                    CurrencyConverter.data[l[0][i]] = (l[2][i], float(l[3][i].replace(",", ".")) / int(l[1][i]))
            except: # internet connection inaccessible
                for t in [("USD", "Доллар США", 73.2056), ("EUR", "Евро", 79.1279)]: # 16.05.2020
                    CurrencyConverter.data[t[0]] = (t[1], t[2])
for i in range(3):
    print(Rectangle(rnd(1, 10), rnd(1, 10)))
c = Calc(10, 5, 5)
print(c.nums())
print(c.sumAll())
print(c.subAll())
print(c.mulAll())
print(c.pow())
print(c.div())
c = Calc(10, 0, 5)
print(c.nums())
print(c.div())
c = CurrencyConverter(1000)
for currency in c:
    print(c[currency])