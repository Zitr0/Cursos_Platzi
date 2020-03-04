'''

Se ejecuta hasta que la condicion sea falsa

x = 9

while x < 10:
    print(x)
    x += 1
'''

import random

def run():
    numberFound = False
    randomNumber = random.randint(0, 20)

    while not numberFound:
        number = int(input('Intentar un numero: '))

        if number == randomNumber:
            print('Encontraste el numero y era >> ', number)
            numberFound = True
        elif number > randomNumber:
            print('El numero es mas pequeno')

        else:
            print('el numero es mas grande')



if __name__ == '__main__':
    run()