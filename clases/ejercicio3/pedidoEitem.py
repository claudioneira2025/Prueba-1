# Ejercicio 3 — Pedido e Ítem y Metodo Menu


class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}, Subtotal: ${self.subtotal():.2f}"


class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)
        print(f" Item '{item.nombre}' agregado al pedido.")

    def listar_items(self):
        if self.items:
            print("\n Lista de ítems en el pedido:")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")
        else:
            print("\n No hay ítems en el pedido.")

    def total_pedido(self):
        return sum(item.subtotal() for item in self.items)

    def mostrar_total(self):
        print("\n_________DETALLE DEL PEDIDO__________")
        self.listar_items()
        print(f"\n TOTAL A PAGAR: ${self.total_pedido():.2f}")


#__________________Metodo MENU ________________

def menu():
    print("\n_________SISTEMA DE PEDIDO _________")
    print("1 Agregar un nuevo ítem")
    print("2 Listar ítems del pedido")
    print("3 Mostrar total del pedido")
    print("4 Salir")
    return input("\nSeleccione una opción: ")