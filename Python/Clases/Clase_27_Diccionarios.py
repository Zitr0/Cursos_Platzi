'''
Diccionarios:
son valores de cualquier tipo
se crea con llaves {}

'''
notas = {}

notas['notaUno'] = 5
notas['notaDos'] = 4
notas['notaTres'] = 3
notas['notaCuatro'] = 4
notas['notaCinco'] = 3

sumaNotas = 0

for nota in notas.values():
    sumaNotas += nota
print(sumaNotas)

promedio = sumaNotas / len(notas.values())

print('El promedio es {} '.format(promedio))
'''
for key in notas:
    print(key)

for value in notas.values():
    print(value)

for key,value in notas.items():
    print('llave: {}, valor: {}'.format(key, value))
'''
