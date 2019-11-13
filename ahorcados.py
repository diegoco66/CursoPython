# -*- coding: utf-8 -*-

import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'colombia',
    'developer',
    'teclado',
    'smartphone',
    'platzi'
]

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(raw_input('Escoge una letra: '))

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()