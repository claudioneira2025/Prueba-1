#main ejercicio4 

from clases.ejercicio4.sensorYmediciones import Sensor, menu

# Crear sensor y medicion
nombre_sensor = input("Ingrese el nombre del sensor: ")
sensor = Sensor(nombre_sensor)

while True:
    opcion = menu()

    if opcion == "1":
        try:
            valor = float(input("Ingrese el valor de la medición: "))
            sensor.registrar_medicion(valor)
        except ValueError:
            print(" Ingrese un número válido.")
    elif opcion == "2":
        promedio = sensor.promedio()
        print(f" Promedio de mediciones: {promedio:.2f}")
    elif opcion == "3":
        maximo = sensor.maximo()
        if maximo is not None:
            print(f" Valor máximo: {maximo}")
        else:
            print("No hay mediciones registradas.")
    elif opcion == "4":
        minimo = sensor.minimo()
        if minimo is not None:
            print(f" Valor mínimo: {minimo}")
        else:
            print("No hay mediciones registradas.")
    elif opcion == "5":
        sensor.resumen()
    elif opcion == "6":
        print(" Saliendo del sistema sensores ")
        break
    else:
        print(" Opción no válida. Intentelo de nuevo ")