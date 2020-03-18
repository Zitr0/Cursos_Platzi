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
    words = message.split(' ')
    cypherMessage = []

    for word in words:
        cypherWord = ''
        for letter in word:
            cypherWord += KEYS[letter]

        cypherMessage.append(cypherWord)

    return ' '.join(cypherMessage)


def decypher(message):
    words = message.split(' ')
    decypherMessage = []

    for word in words:
        decypherWord = ''

        for letter in word:

            for key, value in KEYS.items():
                if value == letter:
                    decypherWord += key

        decypherMessage.append(decypherWord)
    return ' '.join(decypherMessage)

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
            message = str(input('Escribe el mensaje a cifrar: '))
            cypherMessage = cypher(message)
            print(cypherMessage)

        elif command == 'd':
            message = str(input('Escribe el mensaje cifrado: '))
            decypherMessage = decypher(message)
            print(decypherMessage)

        elif command == 's':
            print('salir')
            break
            print('==========================')
        else:
            print('Comando no encontrado')




if __name__ == '__main__':
    print('')
    print('         ======================================')
    print('                 Mensajes Cifrados')
    print('         ======================================')
    run()