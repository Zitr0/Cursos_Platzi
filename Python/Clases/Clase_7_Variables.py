
'''
# -*- coding: utf-8-*-
esto se utiliza para validar carecteres especiales en espanol

Palabras reservadas

False,  class,       finally,    is,         return
None,   continue,   for,        lambda,     try
True,   def,        from,       nonlocal,   while
and,    del,        global,     not,        with
as,     elif,       if,         or,         yield
assert, else,       import,     pass        break,
except, in,         raise

'''
'''
x = 'hola' + "hola"
y = 'camilo' * 4
print(x)
print(y)
print(type(x))
print(type(y))

print("--------------------------")
pi = 3.1416
multiplicar = int(input("Ingrese el valor a multiplicar :: "))
exponente = int(input("Ingrese el valor a elevar :: "))
resultado = pi * multiplicar ** exponente
print("El resultado de los valores anteriores es", resultado)
print("--------------------------")

'''
print("-----------------------------------------------------")

name = input("Ingresa tú nombre > ")
print(type(name))
print("Hola, " + name + "!")

print("-----------------------------------------------------")

