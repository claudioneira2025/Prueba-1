
class SistemaAutenticacion:
    def __init__(self):
        """Inicializa el sistema con un diccionario vacío de usuarios."""
        self.usuarios = {}

    def registrar_usuario(self, nombre_usuario, contraseña):
        """Registra un nuevo usuario si no existe previamente."""
        if nombre_usuario in self.usuarios:
            print(f"El nombre de usuario '{nombre_usuario}' ya está registrado.")
        else:
            self.usuarios[nombre_usuario] = contraseña
            print(f" Usuario '{nombre_usuario}' registrado correctamente.")

    def iniciar_sesion(self, nombre_usuario, contraseña):
        "Valida las credenciales del usuario e inicia sesión si son correctas"
        if nombre_usuario not in self.usuarios:
            print(f" El usuario '{nombre_usuario}' no existe.")
        elif self.usuarios[nombre_usuario] != contraseña:
            print(" Contraseña incorrecta. Acceso denegado.")
        else:
            print(f" Bienvenido, {nombre_usuario}. Acceso autorizado.")

    def consultar_usuario(self, nombre_usuario):
        "Consulta si un usuario está registrado"
        if nombre_usuario in self.usuarios:
            print(f" El usuario '{nombre_usuario}' está registrado.")
        else:
            print(f" El usuario '{nombre_usuario}' NO está registrado.")

    def menu(self):
        "Muestra el menú principal del sistema"
        while True:
            print("\n MENÚ PRINCIPAL \n")
            print("1 Registrar nuevo usuario")
            print("2 Iniciar sesión")
            print("3 Consultar usuario")
            print("4 Salir")
            
            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                nombre = input("Ingrese nombre de usuario: ")
                contraseña = input("Ingrese contraseña: ")
                self.registrar_usuario(nombre, contraseña)

            elif opcion == "2":
                nombre = input("Ingrese nombre de usuario: ")
                contraseña = input("Ingrese contraseña: ")
                self.iniciar_sesion(nombre, contraseña)

            elif opcion == "3":
                nombre = input("Ingrese nombre de usuario: ")
                self.consultar_usuario(nombre)

            elif opcion == "4":
                print(" Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print(" Opción no válida. Intente nuevamente.")


# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaAutenticacion()
    sistema.menu()