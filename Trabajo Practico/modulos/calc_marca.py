def calc_marca (h_lar,m_lar,s_lar,h_lleg,m_lleg,s_lleg):
    '''toma por parametros 6 valores, en los cuales los primeros tres
    valores corresponden al horario de largada, y los ultimos 3 corresponden al horario de
    llegada. Define una variable para estos 2 horarios los cuales son resultados
    de la conversion de horas, minutos y segundos a segundos. Realiza la
    diferencia entre el horario de llegada y largada y mediante la definicion
    de otra variable los vuelve a convertir, de segundos a horas, minutos y
    segundos para luego devolver dichos valores.'''
    larg_s=h_lar*3600+m_lar*60+s_lar
    lleg_s=h_lleg*3600+m_lleg*60+s_lleg
    marca=lleg_s-larg_s
    h_marca=marca/3600
    m_marca=((marca-(h_marca*3600))/60)
    s_marca=marca-(h_marca*3600+m_marca*60)
    return h_marca,m_marca,s_marca