def firstNotRepeat(charSequence):
    seenLetter = {}

    for idx, letter in enumerate(charSequence):
        if letter not in seenLetter:
            seenLetter[letter] = (idx, 1)
        else:
            seenLetter[letter] = (seenLetter[letter][0], seenLetter[letter][1] + 1)

    finalLetters = []
    for key, value in seenLetter.items():
        if value[1] == 1:
            finalLetters.append((key, value[0]))

    notRepeat = sorted(finalLetters, key=lambda value: value[1])

    if notRepeat:
        return notRepeat[0][0]
    else:
        return '_'

if __name__ == '__main__':
    charSequence = str(input('Escribir una secuencia de caracteres: '))

    result = firstNotRepeat(charSequence)

    if result == '_':
        print('Todos los caracteres se repiten')
    else:
        print('El primer caracter NO repetido es: {}'.format(result))