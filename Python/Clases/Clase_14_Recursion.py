'''
Una función puede llamarse así misma
dentro del bloque

'''

def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


if __name__ == '__main__':
    number = int(input('Ingresar el número: '))

    resultado = factorial(number)
    print(resultado)