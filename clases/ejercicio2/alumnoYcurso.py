


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
            print(f"El alumno {alumno} ya está inscrito en el curso")
        else:
            self.alumnos.append(alumno)
            print(f"Alumno {alumno} inscrito correctamente en el curso {self.nombre}")

    def remover_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            print(f"Alumno {alumno} removido del curso {self.nombre}")
        else:
            print(f"El alumno {alumno} no está inscrito en el curso {self.nombre}")

    def listar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos inscritos en este curso")
        else:
            print(f"Alumnos inscritos en el curso '{self.nombre}':")
            for i, alumno in enumerate(self.alumnos, start=1):
                print(f"  {i}. {alumno}")

    def mostrar_estado(self):
        print("\nEstado del curso:")
        print(f"Nombre del curso: {self.nombre}")
        print(f"Total de alumnos: {len(self.alumnos)}")
        self.listar_alumnos()