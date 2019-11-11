""" Dada una altura introducida por el usuario,
realiza un programa que pinte una pirámide a base de asteriscos
con la altura indicada."""

print("Este programa dibuja una pirámide")
alturaintroducida = int(input("Introduzca la altura de la pirámide:"))
i = 1
j = 10

planta = 1
longitudDeLinea = 1
while i <= alturaintroducida:
    j = i
    for esp in range(alturaintroducida-i,0,-1):
        print(" ",end='')
    for j in range(i, 0, -1):
        print(" *", end = '')
    print ("\n", end='')
    i = i + 1
