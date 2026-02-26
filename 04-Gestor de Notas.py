# Creo un diccionario vacio
diccionario = {}

# Creo funciones para cada opcion
def listo_alumnos():
    if len(diccionario.values()) == 0:
        print('\nNo existen notas aun\n')
        constructor()
    else:
        print('\n')
        print('-'*50)
        for alumno, nota in diccionario.items():
            print(f'{str(alumno).capitalize()} : {nota}')
        print('-'*50)
        print('\n')
        constructor()

def agrego_alumno():
    alumno = input('\nNombre del alumno:').lower()
    nota = input('Nota del alumno:')
    print('\n')

    if alumno in diccionario.keys():
        print('\nYa esta')
        input('presione una tecla para continuar')
        constructor()
    else:
        diccionario[alumno] = nota
        constructor()

def elimino_alumno():
    alumno = input('\nNombre del alumno:').lower()
    if alumno in diccionario.keys():
        diccionario.pop(alumno)
        print('\nEliminado con exito')
        input('presione una tecla para continuar')
        constructor()
    else:
        print('\nNo esta')
        input('presione una tecla para continuar')
        constructor()

# Creo constructor
def constructor():
    print('-'*50)
    print('Bienvenido al gestor de notas')
    print('-'*50)
    accion = int(input('''
Indique la opcion a escoger:
    1-Mostrar Notas
    2-Agregar Alumno
    3-Eliminar Alumno\n'''))

    if accion == 1:
        listo_alumnos()
    elif accion == 2:
        agrego_alumno()
    elif accion == 3:
        elimino_alumno()

constructor()