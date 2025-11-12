#ejercicio7 clases y metodo menu

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} - Tel: {self.telefono}, Correo: {self.correo}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f" Contacto '{contacto.nombre}' agregado a la agenda.")

    def mostrar_contactos(self):
        if self.contactos:
            print("\n Lista de contactos:")
            for i, contacto in enumerate(self.contactos, start=1):
                print(f"{i}. {contacto}")
        else:
            print("\n La agenda está vacía.")

    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if encontrados:
            print("\n Contactos encontrados:")
            for c in encontrados:
                print(c)
        else:
            print(f" No se encontró ningún contacto con el nombre '{nombre}'.")

    def eliminar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if encontrados:
            for c in encontrados:
                self.contactos.remove(c)
            print(f" Contacto(s) '{nombre}' eliminado(s) de la agenda.")
        else:
            print(f" No se encontró ningún contacto con el nombre '{nombre}'.")

#___________menu____________

def menu():
    print("\n   SISTEMA DE AGENDA   \n")
    print("1- Agregar nuevo contacto")
    print("2- Mostrar todos los contactos")
    print("3- Buscar contacto por nombre")
    print("4- Eliminar contacto por nombre")
    print("5- Salir de Agenda")
    return input("\n Seleccione una opción: ")



