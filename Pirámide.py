""" Dada una altura introducida por el usuario,
realiza un programa que pinte una pirámide a base de asteriscos
con la altura indicada."""

print("Este programa dibuja una pirámide")
alturaintroducida = (int input("Introduzca la altura de la pirámide:"))

planta = 1
longitudDeLinea = 1
espacios = alturaintroducida - 1

while planta <= alturaintroducida:
    """ Inserta espacios """
