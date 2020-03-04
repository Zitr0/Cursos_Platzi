'''
substring  slices

rangos que se requieren y los saltos necesarios

'''


my_string = 'camilo'
print(my_string[1:])

print(my_string[1:3])
print(my_string[1:5])    # el hace el recorrido pero llega hasta el caracter indicado, menos uno
print(my_string[1:6:2])  # Se pone al final los pasos que se quiere saltar
print(my_string[::-1])   # Recorre todo al reves