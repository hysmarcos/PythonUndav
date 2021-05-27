def validar_inscripcion(num):
    '''La funcion validar_inscripcion toma por parametro un valor que
    corresponde al numero de inscripcion del participante, verifica que
    este sea mayor que 0, mientras el valor no cumpla dicha restriccion,
    en caso de ser 0 solicitará la confirmacion del dato. de ser afirmativa
    la respuesta devuelve el valor confirmado sino, en caso de no confirmarlo
    o que el valor ingresado sea menor a 0 se solicita el reingreso '''
    while num<=0:
        if num==0:
            rta=(input("Desea confirmar el dato? [S/N]: "))
            if rta=="S":
                return num
            else:
                num=(eval(input("Ingrese nuevamente el número de competidor: " )))
        elif num<0:
            num=(eval(input("El numero no puede ser negativo. reingreselo: ")))
    return num