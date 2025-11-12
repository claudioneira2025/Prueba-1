
#___Main ejercicio3 Pedido Item se importa clases y metodo menu
from clases.ejercicio3.pedidoEitem import Item, Pedido, menu

pedido = Pedido()

while True:
    opcion = menu()

    if opcion == "1":
        nombre = input("Ingrese el nombre del ítem: ")
        try:
            precio = float(input("Ingrese el precio del ítem: "))
            cantidad = int(input("Ingrese la cantidad del ítem: "))
        except ValueError:
            print(" Precio y cantidad deben ser números válidos.")
            continue
        item = Item(nombre, precio, cantidad)
        pedido.agregar_item(item)

    elif opcion == "2":
        pedido.listar_items()

    elif opcion == "3":
        pedido.mostrar_total()

    elif opcion == "4":
        print(" Saliendo del sistema Item y Pedidos")
        break

    else:
        print(" Opción no válida. Intentelo de nuevo ")