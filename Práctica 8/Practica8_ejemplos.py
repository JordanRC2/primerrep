# --------- PRÁCTICA 8 _ EJEMPLOS -----------
import numpy as np

# Ejemplo 1
a = np.array([(1,2,3),(4,5,6)])
print(a)
print()
a = a + 1 # Suma de una matriz más un escalar
print(a)
print()

#Ejemplo 2
b = np.array([(4,5,6),(7,8,9)])
print(b)
print()
b = b-2 #Resta de una matriz menos un escalar
print(b)
print()

#Ejemplo 3
c = np.array([(5,4,3),(8,7,6)])
print(c)
print()

c = c*2 #Multiplicación de una matriz por un escalar
print(c)
print()

#Ejemplo 4
d = np.array([(2,2,2),(6,6,6)])
print(d)
print()
d = d/2 # División de una matriz sobre un escalar
print(d)
print()

#Ejemplo 5
e = np.array([(5,6,7),(2,3,4)])
print(e)
print()
e = e**2 # Potencia de una matriz
print(e)
print()

#Ejemplo 6
A = np.array([(5,6,7),(1,2,3)])
B = np.ones((2,3))
print(A)
print(B)
print()
resultado = A+B # Suma de matrices del mismo tamaño
print(resultado)

#Ejemplo 7
A = np.array([(5,6,7),(1,2,3)])
B = np.ones((2,3))
print(A)
print(B)
print()
resultado = A-B # Resta de matrices del mismo tamaño
print(resultado)

#Ejemplo 8
A = np.array([(5,6,7),(1,2,3)])
B = np.ones((3,3))
print(A)
print(B)
print()
resultado = A@B # Multiplicación de matrices
print(resultado)





