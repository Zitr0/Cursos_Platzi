'''
Juego Ahorcado

en Mayusculas las constantes

'''

import random


IMAGES = [
'''
    *---*
    |   |
        |
        |
        |
        |
        |
        ===========''', '''

    *---*
    |   |
    O   |
        |
        |
        |
        |
        ===========''', '''

    *---*
    |   |
    O   |
    |   |
        |
        |
        |
        ===========''', '''

    *---*
    |   |
    O   |
   /|   |
        |
        |
        |
        ===========''', '''

    *---*
    |   |
    O   |
   /|\  |
        |
        |
        |
        ===========''', '''

    *---*
    |   |
    O   |
   /|\  |
    |   |
        |
        |
        ===========''', '''

    *---*
    |   |
    O   |
   /|\  |
    |   |
   /    |
        |
        ===========''', '''

    *---*
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        |
        ===========''', '''
    '''
]

WORDS = [
        'celular',
        'monitor',
        'computador',
        'teclado',
        'mouse',
        'gafas',
        'cuaderno',
        'tablet'
]


# Se define una función para obtener una palabra, dentro de la lista
# Palabras, esto se obtiene por el indice


def randomWord():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def displayBoard(hiddenWord, tries):
    print(IMAGES[tries])
    print('')
    print(hiddenWord)
    print('--- * --- * --- * --- * --- * ---')


def run():
    word = randomWord()
    # Se muestra la palabra escondida con guion bajo
    hiddenWord = ['_'] * len(word)
    tries = 0

    while True:
        #Muestra tablero con 2 parametros
        displayBoard(hiddenWord, tries)
        currentLetter = str(input('Escribir una letra: '))
    pass


if __name__ == '__main__':
    print(':: Bienvenidos al juego ::')
    run()
