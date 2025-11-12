#Main ejercicio 6

from clases.ejercicio6.usuarioYautenticacion import Usuario,SistemaUsuarios, menu

sistema = SistemaUsuarios()

while True:
    opcion = menu()

    if opcion == "1":
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        sistema.registrar_usuario(nombre_usuario, contraseña)

    elif opcion == "2":
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        sistema.iniciar_sesion(nombre_usuario, contraseña)

    elif opcion == "3":
        nombre_usuario = input("Ingrese el nombre de usuario a consultar: ")
        if sistema.usuario_registrado(nombre_usuario):
            print(f" El usuario '{nombre_usuario}' está registrado.")
        else:
            print(f" El usuario '{nombre_usuario}' no está registrado.")

    elif opcion == "4":
        print(" Saliendo del sistema Usuarios y Autenticacion Gracias")
        break

    else:
        print(" Opción no válida. Intentelo de nuevo ")