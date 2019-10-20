# -*- coding: utf-8 -*-

def run():
    number = int(raw_input('Escribe un número: '))
    factor = factorial(number)
    print(factor)

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

if __name__ == '__main__':
    run()