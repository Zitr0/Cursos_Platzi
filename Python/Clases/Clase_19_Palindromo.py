'''
Si una palabra es lo mismo al derecho y al reves

'''

def palindrome(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True

    return False

if __name__ == '__main__':
    word = str(input('Escribe una palabra'))

    result = palindrome(word)

    if result == True:
        print('{} es un palindromo.'.format(word))
    else:
        print('{} no es un palindromo.'.format(word))
