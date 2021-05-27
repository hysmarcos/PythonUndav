'''
Escribir un programa que le pida al usuario que ingrese una sucesión de velocidades
alcanzadas por el cohete Ariane 5 (primero una velocidad, luego otra, y así siguiendo), desde
su lanzamiento hasta el desprendimiento del satélite Arsat-2, hecho informado mediante el
ingreso del valor -1. Al final, el programa debe imprimir las velocidades mínima y máxima
alcanzadas por el Ariane 5 durante el trayecto informado. [No es necesario validar los datos]
'''

def velocidades():
    velocidad=eval(input("Ingrese el valor actual de la velocidad del cohete [El valor -1 finaliza el programa]: "))
    vel_min=velocidad
    vel_max=velocidad
    while velocidad!=-1:
        if vel_min>velocidad:
            vel_min=velocidad
        if vel_max<velocidad:
            vel_max=velocidad
        velocidad=eval(input("Ingrese el valor actual de la velocidad del cohete [El valor -1 finaliza el programa]: "))
    print("La velocidad minima alcanzada por el cohete desde su lanzamiento es de: ", vel_min, "\nLa velocidad maxima alcanzada por el cohete hasta el desprendimiento del satelite es de: ", vel_max)
velocidades() 