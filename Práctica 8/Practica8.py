import numpy as np #agregamos y renombramos libreria

# Estructura tipo array

x = np.array([1,5,9]) # declaramos un vector fila
print(x)

#Declaramos una matriz de 2x3
matriz = np.array([[1,3,6],[8,9,10]])
print(matriz)

print(matriz.size) #Conocemos el número de elementos de la matriz
print(matriz.shape) # Conocemos el número de filas y columnas

# Generamos una lista de números que va desde el 0 hasta el 10
# con incrementos de 1 en 1
arreglo_datos = np.arange(0,11,1)
print(arreglo_datos)

# Generamos una lista de números desde el -5 hasta el 7.5
# con incrementos de 0.5
arreglo_datos2 = np.arange(-5,7.5,0.5)
print(arreglo_datos2)

# Accedemos a un valor específico de la matriz
print(matriz[0,1]) #fila, columna
# Accedemos al valor de toda la fila
print(matriz[0,:])
# Accedemos a los valores de la última columna
print(matriz[:,-1])

matriz_ceros = np.zeros((2,2))
print(matriz_ceros)

matriz_unos = np.ones((3,3))
print(matriz_unos)

matriz_identidad = np.identity(4)
print(matriz_identidad)
