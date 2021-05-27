'''
Desarrollar en Python y explicar en palabras :
a. Definir una función, denominada “dados_3”, que reciba en sus parámetros tres números, que
representan los valores de tres dados, y que devuelva un resultado en caracteres, según sea
una de las siguientes condiciones [No es necesario validar los datos]:

‘I2’, si exactamente dos, de los tres valores, son iguales entre sí
‘I3’, si todos los valores son iguales entre sí
‘D’, si los tres valores son distintos entre sí.
Ejemplos:

para los valores 3, 1 y 3 la función debería devolver el valor “I2”
para los valores 5, 5 y 5 la función debería devolver el valor “I3”
para los valores 1, 3 y 5 la función debería devolver el valor “D”
Dé un ejemplo de invocación y utilización de la función “dados_3”.
'''

def dados_3(n1,n2,n3):
    if n1==n2==n3:
        print("I3")    
    elif n1==n2 or n1==n3 or n2==n3:
        print("I2")
    else:
        print("D")
dados_3(n1=eval(input("Valor n1: ")),n2=eval(input("Valor n2: ")),n3=eval(input("Valor n3: ")))