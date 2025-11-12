#main_ejercicio2 se importa clases y menu 

from clases.ejercicio2.alumnoYcurso import Curso, Alumno, menu

curso = None

while True:
    opcion = menu()

    if opcion == "1":
        nombre_curso = input("Ingrese el nombre del curso: ")
        curso = Curso(nombre_curso)
        print(f" Curso '{nombre_curso}' creado correctamente.")

    elif opcion == "2":
        if curso is None:
            print(" Primero debe crear un curso (opción 1).")
        else:
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            alumno = Alumno(nombre_alumno)
            curso.inscribir_alumno(alumno)

    elif opcion == "3":
        if curso is None:
            print(" Primero debe crear un curso (opción 1).")
        else:
            nombre_alumno = input("Ingrese el nombre del alumno a remover: ")
            alumno = Alumno(nombre_alumno)
            curso.remover_alumno(alumno)

    elif opcion == "4":
        if curso is None:
            print(" Primero debe crear un curso (opción 1).")
        else:
            curso.listar_alumnos()

    elif opcion == "5":
        if curso is None:
            print(" Primero debe crear un curso (opción 1).")
        else:
            curso.estado_curso()

    elif opcion == "6":
        print(" Saliendo del sistema de Cursos y Alumnos ")
        break

    else:
        print(" Opción no válida. Intentelo de nuevo ")