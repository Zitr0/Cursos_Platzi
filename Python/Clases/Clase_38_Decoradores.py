'''

Es agregar una funcionalidad a una función

def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        #Acciones a realizar
        print("cualquier cosa")
        funcion_parametro()

        #mas acciones
        print("mas cosas")

    return funcion_interior

@funcion_decoradora
def suma()
    print(1+1)

suma()

'''


def protected(func):

    def wrapper(password):

        if password == 'camilo':
            return func()
        else:
            print('la contrasena es incorrecta')

    return wrapper

@protected
def protected_func():
    print('tu contrasena es correcta.')


if __name__=='__main__':
    password = input('Ingresa tu contrasena: ')

    #wrapper = protected(protected_func)
    #wrapper(password)

    protected_func(password)
