
#clases almuno curso y metodo menu
#_________________ CLASES________________ 

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir_alumno(self, alumno):
        if alumno in self.alumnos:
            print(f" El alumno '{alumno}' ya está inscrito en el curso '{self.nombre}'.")
        else:
            self.alumnos.append(alumno)
            print(f" Alumno '{alumno}' inscrito en el curso '{self.nombre}' correctamente.")

    def remover_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            print(f" Alumno '{alumno}' ha sido removido del curso '{self.nombre}'.")
        else:
            print(f" No se puede remover: el alumno '{alumno}' no está inscrito en el curso '{self.nombre}'.")

    def listar_alumnos(self):
        if self.alumnos:
            print(f"\n Alumnos inscritos en el curso '{self.nombre}':")
            for alumno in self.alumnos:
                print(f"  - {alumno}")
        else:
            print(f"\n No hay alumnos inscritos en el curso '{self.nombre}'.")

    def estado_curso(self):
        print(f"\n Estado actual del curso '{self.nombre}':")
        self.listar_alumnos()


#_______________MENÚ_________________ 

def menu():
    print("\n INGRESO DE DATOS DE CURSOS Y ALUMNOS \n ")
    print("1 Definir nuevo curso")
    print("2 Registrar nuevo alumno e inscribirlo")
    print("3 Remover alumno del curso")
    print("4 Listar alumnos inscritos")
    print("5 Consultar estado del curso")
    print("6 Salir del Menu")
    return input("\nSeleccione una opción: ")