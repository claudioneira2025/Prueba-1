#Main ejercicio 7

from clases.ejercicio7.agendaYcontacto import Agenda, Contacto, menu

agenda = Agenda()

while True:
    opcion = menu()

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono: ")
        correo = input("Ingrese el correo electrónico: ")
        contacto = Contacto(nombre, telefono, correo)
        agenda.agregar_contacto(contacto)

    elif opcion == "2":
        agenda.mostrar_contactos()

    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)

    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        agenda.eliminar_contacto(nombre)

    elif opcion == "5":
        print(" Saliendo de Agenda")
        break

    else:
        print(" Opción no válida. Intentelo de nuevo ")