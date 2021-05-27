def validar_edad (num1):
    '''La funcion validar_edad toma por parametro un valor que corresponde a la edad del
    participante, el cual debe estar comprendido entre los 18 y 65 años, mientras el valor no
    cumpla dicha restriccion, el usuario debera reingresarlo, luego devuelve el valor correcto'''
    while 18>num1>65:
        num1=eval(input("La edad debe estar comprendida entre los 18 y 65 años.\nVuelva a ingresar la edad: "))
    return num1