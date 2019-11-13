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

        letter_indexes = getLetterIndexes(word, current_letter)

        if len(letter_indexes) == 0:
            tries += 1

            if youLose(hidden_word, tries, word):
                break

        else:
            showValidLetters(current_letter, letter_indexes, hidden_word)
            letter_indexes = []

        if youWin(hidden_word, word):
            break

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')

def getLetterIndexes(word, current_letter):
    letter_indexes = []
    for idx in range(len(word)):
        if word[idx] == current_letter:
            letter_indexes.append(idx)

    return letter_indexes

def youLose(hidden_word, tries, word):
    if tries == 7:
        display_board(hidden_word, tries)
        print('')
        print('¡Perdiste! La palabra correcta era {}'.format(word))
        return True
    else:
        return False

def showValidLetters(current_letter, letter_indexes, hidden_word):
    for idx in letter_indexes:
        hidden_word[idx] = current_letter

def youWin(hidden_word, word):
    try:
        hidden_word.index('-')
        return False
    except ValueError:
        print('')
        print('Felicidades! Ganaste. La palabra es: {}'.format(word))
        return True

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()