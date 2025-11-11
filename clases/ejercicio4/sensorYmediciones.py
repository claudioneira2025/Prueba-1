# Ejercicio 4 — Sensor y Mediciones

class Sensor:
    def __init__(self, nombre):
        "Define un nuevo sensor con su nombre y una lista vacía de mediciones"
        self.nombre = nombre
        self.mediciones = []

    def registrar_medicion(self, valor):
        "Registra una nueva medición para el sensor"
        self.mediciones.append(valor)
        print(f" Medición {valor} registrada para el sensor '{self.nombre}'.")

    def obtener_promedio(self):
        "Devuelve el promedio de las mediciones registradas"
        if not self.mediciones:
            print(" No hay mediciones registradas para calcular el promedio.")
            return None
        return sum(self.mediciones) / len(self.mediciones)

    def obtener_maximo(self):
        "Devuelve el valor máximo registrado"
        if not self.mediciones:
            print(" No hay mediciones registradas para obtener el valor máximo.")
            return None
        return max(self.mediciones)

    def obtener_minimo(self):
        "Devuelve el valor mínimo registrado"
        if not self.mediciones:
            print(" No hay mediciones registradas para obtener el valor mínimo.")
            return None
        return min(self.mediciones)

    def mostrar_resumen(self):
        "Muestra el nombre del sensor y un resumen de sus mediciones"
        print(f"\n Sensor: {self.nombre}")
        if not self.mediciones:
            print(" No hay mediciones registradas aún.")
        else:
            promedio = self.obtener_promedio()
            maximo = self.obtener_maximo()
            minimo = self.obtener_minimo()

            print(f" Mediciones registradas: {self.mediciones}")
            print(f" Promedio: {promedio:.2f}")
            print(f" Máximo: {maximo}")
            print(f" Mínimo: {minimo}")
