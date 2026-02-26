from math import sqrt       # libreria matematica para la division

# Declaro funciones de operaciones matematicas
def suma(num_1, num_2):
    return num_1 + num_2

def resta(num_1, num_2):
    return num_1 - num_2

def multiplicacion(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    return num_1 / num_2

def cuadrado(num):
    return num ** 2

def raiz(num):
    return sqrt(num)


# Bienvenida a la app
print('\n' + '-'*50)
print('Calculadora Cientifica:')
print('-'*50)

# Funcion principal que realiza todo e inicia si el numero insertado es una opcion
def calculadora():
    
    operacion = int(input('''
Indique la operacion a realizar:
    1 - Suma
    2 - Resta
    3 - Multiplicacion
    4 - Division
    5 - Cuadrado
    6 - Raiz Cuadrada\n'''))

    if operacion == 1:
        num_1 = int(input('\nPrimer Numero:\t'))
        num_2= int(input('Segundo Numero:\t'))
        print(f'\n{num_1} + {num_2} = {suma(num_1,num_2)}')

    elif operacion == 2:
        num_1 = int(input('\nPrimer Numero:\t'))
        num_2= int(input('Segundo Numero:\t'))
        print(f'\n{num_1} - {num_2} = {resta(num_1,num_2)}')

    elif operacion == 3:
        num_1 = int(input('\nPrimer Numero:\t'))
        num_2= int(input('Segundo Numero:\t'))
        print(f'\n{num_1} * {num_2} = {multiplicacion(num_1,num_2)}')

    elif operacion == 4:
        num_1 = int(input('\nPrimer Numero:\t'))
        num_2= int(input('Segundo Numero:\t'))
        print(f'\n{num_1} / {num_2} = {division(num_1,num_2)}')

    elif operacion == 5:
        num_1 = int(input('\nNumero:\t'))
        print(f'\n{num_1} ** 2 = {cuadrado(num_1)}')

    elif operacion == 6:
        num_1 = int(input('\nNumero:\t'))
        print(f'\nraiz cuadrada({num_1}) = {raiz(num_1)}')

    else :
        print('Numero incorrecto, verifique')
        calculadora()

calculadora()