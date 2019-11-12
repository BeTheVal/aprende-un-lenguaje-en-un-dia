"""Realiza un programa que rellene un array (o una estructura similar)
con 20 números enteros aleatorios entre 1 y 100 y que seguidamente los
muestre por pantalla. A continuación, se deben pasar los números primos
a las primeras posiciones del array y los no primos a las posiciones restantes. 
Muestra finalmente el array resultado. """
import numpy as np
import random

n = 20
aleatorios = [random.randint(1, 100) for _ in range(n)]
print("Esta lista contiene 20 números aleatorios del 1 al 100: ")
print(aleatorios)


""" Falta crear otra lista donde los primos de la lista "aleatorios" vayan primero"""
def esPrimo(l):
    primos = []
    for i in l:
        p = 0
        if i == 1:
          primos.append(i)
        else:
          for j in range(1,i+1):
            if i % j == 0:
              p += 1
          if p == 2:
            primos.append(i)
    return primos

lista = aleatorios
primos = esPrimo(lista)

for x in range(len(lista)):
    c=0
    control = False
    for y in range(len(primos)):
        if lista[x]!=primos[c]:
           control=True
           c+=1
        else:
            control=False

    if control== True:
        primos.append(lista[x])
print("\nEsta es la lista con los primos al principio")
print (primos)