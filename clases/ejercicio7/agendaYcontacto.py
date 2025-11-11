class Contacto:
    "Representa un contacto con nombre, teléfono y correo"
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def datos_contacto(self):
        "Devuelve una representación legible del contacto"
        return f" Nombre: {self.nombre} |  Teléfono: {self.telefono} |  Correo: {self.correo}"


class Agenda:
    "Gestiona una lista de contactos"
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, correo):
        "Agrega un nuevo contacto a la agenda"
        # Verificar si el contacto ya existe por nombre
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f" El contacto '{nombre}' ya existe en la agenda.")
                return
        nuevo = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo)
        print(f" Contacto '{nombre}' agregado correctamente.")

    def mostrar_contactos(self):
        "Muestra todos los contactos de la agenda"
        if not self.contactos:
            print(" La agenda está vacía.")
        else:
            print("\n LISTADO DE CONTACTOS \n")
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        """Busca un contacto por nombre."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(" Contacto encontrado:")
                print(contacto)
                return
        print(f" No se encontró ningún contacto con el nombre '{nombre}'.")

    def eliminar_contacto(self, nombre):
        "Elimina un contacto por su nombre"
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f" Contacto '{nombre}' eliminado correctamente.")
                return
        print(f" No se encontró ningún contacto con el nombre '{nombre}'.")



