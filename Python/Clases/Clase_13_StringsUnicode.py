'''

la comparación en lexicografica
a b c d
1 2 3 4

ASCII  128 caracteres
UNICODE incluye caracteres especiales
Python 2, asume que los string están en ASCII
Python 3, en UNICODE

Utilizar
# -*- coding: utf-8 -*-

'''

s = 'hola'
r = 'p' + s[1:]

nameOne = 'juan'
nameTwo = 'camilo'

Igualdad  = nameOne == nameTwo
Mayor = nameOne > nameTwo
Menor = nameTwo < nameOne     # Se valida desde el primer caracter NO ES por la cantidad de caracteres del string

print (r, Igualdad , Mayor, Menor)

