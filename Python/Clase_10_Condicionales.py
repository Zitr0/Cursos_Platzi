'''
Se evalua como true o false
relacionales
 ==
 !=
 >
 >=
 <
 <=

lógicos
and
or
not
'''

x = 10 == 10
y = 'a' == 'A'
z = 10 > 15
letra = 'a' > 'b'  #Comparación lexicografica, las letras tienen el valor númerico a = 1, b = 2........
print(letra)
prueba = 10 > 15 and 15 > 20

test = 'a' == 'a' or 'b' != 'b'
print(test)


def sayHello(age):
    if age  > 18:
        print('Hola Sr')
    else:
        print('Hola nino')

age = int(input('Ingresar edad : '))

if __name__ == '__main__':
    sayHello(age)