# Programa para adivinar un numero que es generado de forma
# aleatoria entre el uno y el 10 con intentos liimitados.

# importo libreria random para generar el numero de forma aleatoria
import random

# Genero el numero entre el 1-10
numero = random.randrange(1,10)

print('\n' + '-'*50)
print('Bienvenido al juego: Adivina el numero')
print('-'*50)

print('Tiene 3 intentos para adivinar un numero entre el 1-10')

# ciclo for que itera entre el numero de intentos hasta terminar en el 3
for intentos in range(1,4):
    numero_usuario = int(input(f'\nIntento {intentos}:\n'))

    # condiciono lo que sucede si el numero es correcto y rompe el ciclo
    if numero_usuario == numero:
        print(f'\nFelicidades!\nHaz Ganado en {intentos} {'intento' if intentos == 1 else 'intentos'}!\n')
        break

    # segunda condicion que se activa cuando intentos == 3
    elif intentos == 3:
        print(f'\nLo siento ... el numero era {numero}\nvuelva a probar a lo mejor tiene suerte\n')