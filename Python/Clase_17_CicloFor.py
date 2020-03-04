'''
Ciclo For

Iteraciones

break     salir antes de
continue  saltarse
'''

x = range(5, 40, 3)

for i in range(5):
    print(i)

for i in range(5):
    print('Paso', i)

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i**2)

for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break

x = 'Camilo'

for i in range(6):
    if i > 6:
        print('')
    else:
        print(x[i])

