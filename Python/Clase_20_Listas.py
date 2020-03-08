'''

Lista es una secuencia de elementos
permite agrupar varios elementos
se crea con []
se crea con list

'''

def averageTemps(temps):
    sumOfTemps = 0

    for temp in temps:
        sumOfTemps += temp

    return sumOfTemps / len(temps)

if __name__ == '__main__':
    temps = [21 ,24 ,24, 22, 20, 23, 24]

    average = averageTemps(temps)

    print('La temperatura promedio es {}'.format(average))
