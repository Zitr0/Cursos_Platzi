'''
Limites de las funciones

no pueden empezar con digitos
no puede ser palabra reservada
no tener los mismos nombres variables y funciones

Flujo de ejecución


'''


def run():
    print(':: CALCULADORA DE DIVISAS ::')
    print(':: Convierte pesos mexicanos a pesos colombianos. ::')
    print('')

    amount = float(input('Ingresar el valor a convertir : '))

    result = calcular(amount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(amount, result))
    print('')

def calcular(amount):
    mex_to_col = 145.97

    return mex_to_col * amount

if __name__ == '__main__':
    run()
