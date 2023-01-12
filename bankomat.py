class Bankomat:

    def __init__(self):
        self.__saldo = 0

    def spr(self):
        print('Stan konta to', self.__saldo)

    def wplata(self,value):
        self.__saldo += value

    def wyplata(self, value):
        if (self.__saldo - value) < 0:
            print('Niewystarczające środki')
        else:
            self.__saldo -= value

w1 = Bankomat()
print(w1.spr())
w1.wplata(150)
print(w1.spr())
w1.wyplata(100)
print(w1.spr())
w1.wyplata(100)
print(w1.spr())

