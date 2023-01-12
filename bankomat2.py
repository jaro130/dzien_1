class Bankomat:

    def __init__(self):
        __PIN = 1740
        x = int(input('proszę podać PIN: '))
        if x == __PIN:
            self.__saldo = 0
        else:
            while x != __PIN:
                print('PIN nieprawidłowy')
                exit()

    def spr(self):
        print('Stan konta to', self.__saldo)

    def wplata(self, value):
        self.__saldo += value
        print('Stan konta to', self.__saldo)

    def wyplata(self, value):
        if (self.__saldo - value) < 0:
            print('Niewystarczające środki')
        else:
            self.__saldo -= value
            print('Stan konta to', self.__saldo)



w1 = Bankomat()

w1.spr()
w1.wplata(150)
w1.spr()
w1.wyplata(100)
w1.spr()
w1.wyplata(100)
w1.spr()
