import time

from dzialania import dodawanie, odejmowanie, mnozenie, dzielenie


def menu():
    print('Witamy w kalkulatorze, takie działania możesz wykonać:')
    print('1 - dodawanie\t2 - odejmowanie\t\t3 - mnożenie\t4 - dzielenie\t\tq - wyjście z kalkulatora\n')
    wyb = input('Jaką wybrałeś funkcję?: ')
    while wyb != 'q':
        if wyb == '1':
            a = int(input('podaj pierwszą liczbę: '))
            b = int(input('podaj drugą liczbę: '))
            print(f'wynik dodawania {a} i {b} to', dodawanie(a, b),'\n')
            time.sleep(1.5)
            menu()
        elif wyb == '2':
            a = int(input('podaj pierwszą liczbę: '))
            b = int(input('podaj drugą liczbę: '))
            print(f'wynik odejmowania {a} i {b} to',odejmowanie(a, b),'\n')
            time.sleep(1.5)
            menu()
        elif wyb == '3':
            a = int(input('podaj pierwszą liczbę: '))
            b = int(input('podaj drugą liczbę: '))
            print(f'wynik mnożenia {a} i {b} to',mnozenie(a, b),'\n')
            time.sleep(1.5)
            menu()
        elif wyb == '4':
            a = int(input('podaj pierwszą liczbę: '))
            b = int(input('podaj drugą liczbę: '))
            print(f'wynik dzielenia {a} przez {b} to',dzielenie(a, b),'\n')
            time.sleep(1.5)
            menu()
        else:
            print('\nProszę wybrać jedną ze wskazanych pozycji menu')
            menu()
    print('\nDziękujemy za skorzystanie z kalkulatora, życzymy miłego dnia')




menu()


