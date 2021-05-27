'''
Escribir un programa que elija un número al azar, entre 1 y 99, y lo mantenga
en secreto (utilice la función random.randrange (1,100) del módulo random). El programa
debe solicitar al usuario que adivine el número. Si el número que ingresa el usuario es
mayor, el programa debe responder "Incorrecto, mi número es menor"; si el número
ingresado es menor, el programa debe responder "Incorrecto, mi número es mayor". En
ambos casos deberá solicitar otro número hasta que el usuario acierte el correcto. Mostrar la
cantidad de intentos realizados para adivinar.
'''

import random

def num_al_azar():
    x = random.randrange(1,100)    
    num = eval(input("Ingrese un numero del 1 al 99: "))
    intentos = 1
    while num != x:       
        if num > x:
            num = eval(input("Incorrecto, mi numero es menor.\nIngrese un numero del 1 al 99: "))
        else:
            num = eval(input("Incorrecto, mi numero es mayor.\nIngrese un numero del 1 al 99: "))
        intentos+=1 
    print("Su numero de intentos es:", intentos)
num_al_azar()