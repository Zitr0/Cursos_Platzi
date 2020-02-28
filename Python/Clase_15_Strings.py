'''

Secuencia de caracteres
se puede acceder por indice
indices empiezan en cero

0 1 2 3 4 5
c a m i l o

Metodos
upper isupper lower islower find isdigit endswith startswith split join

'''

name = 'Camilo'
validar = name[0]
longitud = len(name)
ultimaLetra  = name[len(name)-1]
mayuscula = name.upper()
minuscula = name.lower()
encontrar = name.find('m')

print(validar , longitud, ultimaLetra, mayuscula, minuscula, encontrar)