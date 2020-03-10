'''
Divisibles por 1 y por si mismos

'''

def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False

    return True

def run():
    pass   # pass = Forma de decir que la función no tiene nada
    number = int(input('Ingresar un numero : '))
    result = isPrime(number)

    if result is True:
        print('El numero -> {} es primo'.format(number))
    else:
        print('El numero -> {} no es primo'.format(number))

if __name__ == '__main__':
    run()