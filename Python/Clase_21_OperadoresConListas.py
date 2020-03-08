'''

Solo se puede utilizar + y *

'''


listaUno = []
listaDos = []

listaUno.append(1)
listaDos.append(4)

resultado = listaUno + listaDos

print(resultado)

resultadoDos = listaUno * 3

print(resultadoDos)


utilesEscolares = ['lapiz','borrador','cuaderno']

del utilesEscolares[0]  #Metodo para eliminar objetos de la lista

print(utilesEscolares)

casa = 'casa'

print(casa)

listaCasa = list(casa)

print(listaCasa)

strCasa = ''.join(listaCasa)

print(strCasa)
