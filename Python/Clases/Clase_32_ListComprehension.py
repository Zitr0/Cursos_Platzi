'''
convierte una secuencia en una nueva secuencia
'''

# List comprehension
pares = [num for num in range(1, 31) if num % 2 == 0]
print(pares)

# Dictionary comprehension
cuadrados = {num: num**2 for num in range(1,11)}
print(cuadrados)

'''
# Creacion de diccionario
cuadrados = {}

for num in range(1,11):
    cuadrados[num] = num**2;

print(cuadrados)
'''

'''

'''

'''

# Creacion de una lista

pares = []

for num in range(1, 31):
    if num % 2 == 0:
        pares.append(num)

print(pares)
'''