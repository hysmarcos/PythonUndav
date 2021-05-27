def validar_hora(h1,m1,s1,h2,m2,s2):
    '''Toma por parametros 6 valores. Los primeros tres y los ultimos 3 corresponden a un determinado horario, representado en horas, minutos y
    segundos. verifica que los ultimos 3 valores sean horarios verdaderos comprendidos en las 24hs, en caso de no serlo,
    solicita el reingreso de aquellos que hayan sido erroneos. el siguiente ciclo verifica que tanto h1 como m1 y s1 sean mayores a h2, m2 y s2 y
    en caso afirmativo solicita el reingreso de aquellos que hayan sido erroneos y devuelve los valores de h2, m2 y s2'''
    while h2>23 or m2>59 or s2>59:
        if h2>23:
            h2=(eval(input("Hora erronea. Reingrese: ")))
        elif m2>59:
            m2=(eval(input("Minutos erroneos. Reingrese: ")))
        else:
            s2=(eval(input("Segundos erroneos. Reingrese: ")))
    while (h1==h2 and m1==m2 and s1>s2) or (h1==h2 and m1>m2) or (h1>h2):
        if (h1>h2):
            h2=eval(input("Hora erronea. Reingrese: "))
        elif (h1==h2 and m1>m2):
            m2=eval(input("Minutos erroneos. Reingrese: "))
        else:
            s2=eval(input("Segundos erroneos. Reingrese: "))
    return h2,m2,s2