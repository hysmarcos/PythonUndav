from modulos.validar_hora import validar_hora
from modulos.validar_inscripcion import validar_inscripcion
from modulos.validar_genero import validar_genero
from modulos.validar_edad import validar_edad
from modulos.calc_marca import calc_marca

def main():
    hic=eval(input("A continuación ingrese el horario de inicio de la competencia. \nIngrese la hora: "))
    mic=eval(input("Ingrese los minutos: "))
    sic=eval(input("Ingrese los segundos: "))
    hic,mic,sic=validar_hora(8,0,0,hic,mic,sic)
    cant_competidores=eval(input("Ingrese la cantidad de competidores inscriptos: "))
    finalistas=0
    menor_marca=(99,99,99)
    total_edades=0
    num_inscripcion=""
    while num_inscripcion!=0:
        num_inscripcion=validar_inscripcion(eval(input("\nIngrese el número del competidor que finalizó el recorrido: ")))
        if num_inscripcion!=0:
            finalistas+=1
            apellido=input("Ingrese el apellido: ")
            nombre=input("Ingrese el primer nombre: ")
            edad=validar_edad(eval(input("Ingrese la edad (en años): ")))
            total_edades+=edad
            genero=validar_genero(input("Ingrese el género [M/F]: "))
            h_lar=eval(input("A continuacion ingrese el horario de largada\nIngrese la hora: "))
            m_lar=eval(input("Ingrese los minutos: "))
            s_lar=eval(input("Ingrese los segundos: "))
            h_lar,m_lar,s_lar=validar_hora(hic,mic,sic,h_lar,m_lar,s_lar)
            h_lleg=eval(input("A continuacion ingrese el horario de llegada\nIngrese la hora: "))
            m_lleg=eval(input("Ingrese los minutos: "))
            s_lleg=eval(input("Ingrese los segundos: "))
            h_lleg,m_lleg,s_lleg=validar_hora(h_lar+2,m_lar,s_lar,h_lleg,m_lleg,s_lleg)
            marca=calc_marca(h_lar,m_lar,s_lar,h_lleg,m_lleg,s_lleg)
            if marca<menor_marca:
                menor_marca=marca  
            print("\nDatos del competidor nº", num_inscripcion)
            print("Apellido y nombre:", apellido,",", nombre)
            print("Edad:", edad)
            print("Genero:",genero)
            print("Hora de largada:", h_lar,":",m_lar,":",s_lar)
            print("Hora de llegada:", h_lleg,":",m_lleg,":",s_lleg)
            #Se cambió "marca" por "marca[0],":",marca[1],":",marca[2]" para que vea mejor en la salida en pantalla
            print("Marca de tiempo:", marca[0],":",marca[1],":",marca[2])          
    print("\nCantidad de competidores:",cant_competidores)
    if finalistas==0:
        print("No hubo finalistas.")
    else:
        #Se cambió "menor_marca" a "menor_marca[0],":",menor_marca[1],":",menor_marca[2]"
        print("Menor marca registrada:",menor_marca[0],":",menor_marca[1],":",menor_marca[2])
        #Se arregló la cuenta para sacar el porcentaje, y se le agregó el signo "%"
        print("Porcentaje de competidores que terminaron el recorrido:", 100.0*finalistas/cant_competidores,"%")
        #Faltaba la salida del promedio de edad
        print("Promedio de edad de finalistas: ", 1.0*total_edades/finalistas)
main()