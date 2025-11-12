
#ejercicio6 clases y metodo menu

class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña


class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre_usuario, contraseña):
        if nombre_usuario in self.usuarios:
            print(f" El usuario '{nombre_usuario}' ya está registrado.")
        else:
            self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contraseña)
            print(f" Usuario '{nombre_usuario}' registrado correctamente.")

    def iniciar_sesion(self, nombre_usuario, contraseña):
        if nombre_usuario not in self.usuarios:
            print(f" Usuario '{nombre_usuario}' no existe.")
            return False
        usuario = self.usuarios[nombre_usuario]
        if usuario.contraseña == contraseña:
            print(f" Acceso autorizado. ¡Bienvenido, {nombre_usuario}!")
            return True
        else:
            print(" Contraseña incorrecta.")
            return False

    def usuario_registrado(self, nombre_usuario):
        return nombre_usuario in self.usuarios


#__________Menu___________

def menu():
    print("\n SISTEMA DE AUTENTICACIÓN DE USUARIOS \n")
    print("1- Registrar nuevo usuario")
    print("2- Iniciar sesión")
    print("3- Consultar si un usuario está registrado")
    print("4- Salir")
    return input("\n Seleccione una opción: ")