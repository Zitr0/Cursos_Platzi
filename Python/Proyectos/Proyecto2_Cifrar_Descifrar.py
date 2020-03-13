'''
Cifrar y descifrar un mensaje
'''

KEYS = {
    'a': 'K',
    'b': 'J',
    'c': 'I',
    'd': 'H',
    'e': 'G',
    'f': 'F',
    'g': 'E',
    'h': 'D',
    'i': 'C',
    'j': 'B',
    'k': 'A',
    'l': '0',
    'm': '9',
    'n': '8',
    'o': '7',
    'p': '6',
    'q': '5',
    'r': '4',
    's': '3',
    't': '2',
    'u': '1',
    'v': '!',
    'w': '?',
    'x': '.',
    'y': ',',
    'z': 'w',
    'A': 'u',
    'B': 'e',
    'C': 'e',
    'D': 'n',
    'E': 'm',
    'F': 'l',
    'G': 'k',
    'H': 'j',
    'I': 'i',
    'J': 'h',
    'K': 'g',
    'L': 'f',
    'M': 'd',
    'N': 'c',
    'O': 'b',
    'P': 'a',
    'Q': 'z',
    'R': 'y',
    'S': 'x',
    'T': 'Z',
    'U': 't',
    'V': 's',
    'W': 'r',
    'X': 'q',
    'Y': 'p',
    'Z': 'o',
    '1': 'L',
    '2': 'M',
    '3': 'N',
    '4': 'O',
    '5': 'P',
    '6': 'Q',
    '7': 'R',
    '8': 'S',
    '9': 'T',
    '0': 'U',
    '.': 'V',
    ',': 'W',
    '?': 'X',
    '!': 'Y',
}

def cypher(message):
    pass

def decypher(message):
    pass

def run():

    while True:
        command = str(input('''
            Bienvenidos a la encriptación
                Que deseas hacer?
              
            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir      
        
        ======================================
        '''))

        if command == 'c':
            print('cifrar')
            print('==========================')
        elif command == 'd':
            print('decifrar')
            print('==========================')
        elif command == 's':
            print('salir')
            print('==========================')
        else:
            print('Comando no encontrado')




if __name__ == '__main__':
    print('')
    print('         ======================================')
    print('                 Mensajes Cifrados')
    print('         ======================================')
    run()