# Ejercicio 3 — Pedido e Ítem

class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        "Calcula el subtotal del ítem (precio * cantidad)"
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} | Precio: ${self.precio} | Cantidad: {self.cantidad} | Subtotal: ${self.calcular_subtotal()}"


class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        """Agrega un ítem al pedido."""
        self.items.append(item)
        print(f"Ítem '{item.nombre}' agregado correctamente al pedido.")

    def listar_items(self):
        "Muestra todos los ítems del pedido con su detalle"
        if not self.items:
            print("El pedido no tiene ítems registrados.")
        else:
            print("\n Detalle del pedido:")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")

    def calcular_total(self):
        "Calcula el total del pedido sumando los subtotales de todos los ítems"
        return sum(item.calcular_subtotal() for item in self.items)

    def mostrar_resumen(self):
        "Muestra el detalle del pedido y el total final a pagar"
        self.listar_items()
        print(f"\nTOTAL A PAGAR: ${self.calcular_total():.2f}")