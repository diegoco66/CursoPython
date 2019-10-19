# -*- coding: utf-8 -*-

def run():
    number = int(raw_input('Escribe un número: '))
    result = is_prime(number)

    if result is True:
        print('Tu número es primo')
    else:
        print('Tu número NO es primo')

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        return check_module(number)

def check_module(number):
    for i in range(3, number):
        if number % i == 0:
            return False

    return True

if __name__ == '__main__':
    run()