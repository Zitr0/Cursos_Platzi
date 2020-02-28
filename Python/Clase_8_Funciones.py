'''
Funciones
Secuencia de comandos agrupados por nombres

palabra reservada   def

ejemplo:
def suma(num1,num2)
    return num1 + num2

'''

import turtle

def main():
    window = turtle.Screen()
    camilo = turtle.Turtle()

    make_square(camilo)
    turtle.mainloop()

def make_square(camilo):
    length = int(input('Tamano cuadrado'))

    for i in range(4):
        make_line_and_turn(camilo, length)

def make_line_and_turn(camilo, length):
    camilo.forward(length)
    camilo.left(90)

if __name__ == '__main__':
    main()
