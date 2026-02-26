# creando programa que indica cual es tu IMC (Indice de Masa Corporal)

print('-'*50)
print('Bienvenido al calculador de Indice de Masa corporal')
print('Para continuar necesito algunos datos:')

# creo las variables que toman el valor de cada pregunta
altura = input('Diga su estatura en metros (m):\n')
peso = input('Diga su peso en kilogramos (kg):\n')

# Combierto en flotante las variables y realizo la operacion
ind_masa_corp = float(peso)/(pow(float(altura),2))

# Imprimo por consola el resultado de forma formateada
print(f'Pues le cuento que su IMC es de {ind_masa_corp}')