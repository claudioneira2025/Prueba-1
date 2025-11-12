# Ejercicio 4 — Sensor, Mediciones y Metodo Menu


class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def registrar_medicion(self, valor):
        self.mediciones.append(valor)
        print(f" Medición {valor} registrada.")

    def promedio(self):
        if self.mediciones:
            return sum(self.mediciones) / len(self.mediciones)
        return 0

    def maximo(self):
        if self.mediciones:
            return max(self.mediciones)
        return None

    def minimo(self):
        if self.mediciones:
            return min(self.mediciones)
        return None

    def resumen(self):
        print(f"\n_______ RESUMEN DEL SENSOR: {self.nombre}_________")
        if self.mediciones:
            print(f"Cantidad de mediciones: {len(self.mediciones)}")
            print(f"Promedio: {self.promedio():.2f}")
            print(f"Máximo: {self.maximo()}")
            print(f"Mínimo: {self.minimo()}")
        else:
            print("No hay mediciones registradas.")

#__________________Metodo Menu____________
def menu():
    print("\n____ SISTEMA DE SENSORES____\n")
    print("1 Registrar nueva medición")
    print("2 Consultar promedio de mediciones")
    print("3 Consultar valor máximo")
    print("4 Consultar valor mínimo")
    print("5 Mostrar resumen del sensor")
    print("6 Salir")
    return input("\nSeleccione una opción: ")