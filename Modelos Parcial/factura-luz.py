'''
Definir una función, denominada “factura_luz”, que reciba como parámetro un número
entero, que representa la cantidad de kilowatt-hora (kWh) consumidos durante el bimestre, y
que devuelva como resultado el costo del consumo, considerando que la tarifa del kWh varía
según se describe [No es necesario validar los datos]:

- si el consumo es menor que 300 kWh, se cobra un cargo fijo de $ 180.
- la tarifa del kWh es $ 0,80 si el consumo es mayor o igual a 300 y menor a 1050.
- la tarifa del kWh es $ 0,96 si el consumo es mayor o igual a 1050 y menor a 1500.
y si el consumo es mayor o igual a 1500, la tarifa del kWh es $ 0,99.

Nota: Cuando el cargo no es fijo, la fórmula es: costo = consumo x tarifa

b. Escribir un programa que le pida al usuario que ingrese, uno a uno, los datos de consumo de
energía eléctrica de los domicilios de la calle Mario Bravo. Por cada domicilio se ingresará el
nro. de puerta y el consumo en kWh, hasta finalizar ingresando el nro. de puerta 0. El
programa debe mostrar el costo de cada consumo, invocando a la función del ítem anterior.
Al final, el programa debe imprimir el monto total facturado y el máximo consumo de kWh
registrado en un domicilio. [No es necesario validar los datos]
'''

def factura_luz(cant_kwh):
    if cant_kwh<300:
        costo=180
    elif cant_kwh>=300 and cant_kwh<1050:
        costo=cant_kwh*0.80
    elif cant_kwh>=1050 and cant_kwh<1500:
        costo=cant_kwh*0.96
    elif cant_kwh>=1500:
        costo=cant_kwh*0.99
    return costo

def main():
    print("En este programa se le va a solicitar que ingrese el consumo de energia electrica de los domicilios de la calle Mario Bravo.\n")
    max_consumo=0
    total=0
    num_puerta=eval(input("Ingrese el numero de puerta [El numero 0 cierra el programa]: "))
    while num_puerta!=0:
        cant_kwh=eval(input("Ingrese el valor de los kWh consumidos: "))
        costo=factura_luz(cant_kwh)
        print("El costo del consumo es de: $", costo)
        total=total+costo
        if max_consumo<cant_kwh:
            max_consumo=cant_kwh
        num_puerta=eval(input("\nIngrese el numero de puerta [Si ingresa el nro. 0, el programa finaliza]: "))
    print("El monto total facturado es de:  $", total)
    print("El máximo consumo registrado en un domicilio es de: ", max_consumo)
main()