def validar_genero(genero):
    '''La funcion validar_edad toma por parametro un valor que corresponde al
    genero del participante, el cual debe ser 'F' o 'M', mientras el valor
    ingresado no cumpla dicha restriccion, el usuario debera reingresarlo,
    luego devuelve el valor correcto'''
    while genero!="M" and genero!="F":
        genero=input("Vuelva a ingresar el genero: ")
    return genero