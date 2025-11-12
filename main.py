

#Ejercicio numero 1 libro y biblioteca


from clases.ejercicio1 import libroYbiblioteca
if __name__ == "__main__":
        biblioteca = libroYbiblioteca.Biblioteca()


while True:
        print("\n MENÚ BIBLIOTECA \n")
        print("1 Registrar nuevo libro")
        print("2 Mostrar catálogo completo")
        print("3 Buscar libro por título")
        print("4 Prestar libro")
        print("5 Devolver libro")
        print("6 Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
                titulo = input("Título del libro: ")
                autor = input("Autor: ")
                copias = int(input("Número de copias disponibles: "))                       
                biblioteca.registrar_libro(titulo, autor, copias)

        elif opcion == "2":
                biblioteca.mostrar_catalogo()

        elif opcion == "3":
                titulo = input("Ingrese el título del libro a buscar: ")
                biblioteca.buscar_libro(titulo)

        elif opcion == "4":
                titulo = input("Ingrese el título del libro a prestar: ")
                biblioteca.prestar_libro(titulo)

        elif opcion == "5":
                titulo = input("Ingrese el título del libro a devolver: ")
                biblioteca.devolver_libro(titulo)

        elif opcion == "6":
                print(" Saliendo del sistema de biblioteca...")
                break
        else:
                print("Opción inválida. Intente nuevamente")




#Termina el primer ejercicio
#-----------------------------------------------------------


#Empiesa 2 ejercico
from clases.ejercicio2 import alumnoYcurso

if __name__ == "__main__":
        curso_colegio = Curso("Básica")

a1 = Alumno("Ana")
a2 = Alumno("Carlos")
a3 = Alumno("Beatriz")

curso_colegio.inscribir_alumno(a1)
curso_colegio.inscribir_alumno(a2)
curso_colegio.inscribir_alumno(a3)

curso_colegio.mostrar_estado()

curso_colegio.remover_alumno(a2)
curso_colegio.remover_alumno(a2)

curso_colegio.mostrar_estado()


#aqui termina el ejercicio 2

#------------------------------------------------------------------


#Ejercicio 3 pedido e item
from clases.ejercicio3 import pedidoEitem
pedido = pedidoEitem.Pedido()

if __name__ == "__main__":
# Crear un nuevo pedido
# Registrar ítems
        item1 = Item("Laptop", 1200.00, 1)
        item2 = Item("Mouse", 25.50, 2)
        item3 = Item("Teclado", 45.00, 1)

# Agregar ítems al pedido
        pedido.agregar_item(item1)
        pedido.agregar_item(item2)
        pedido.agregar_item(item3)

# Mostrar resumen del pedido
        pedido.mostrar_resumen()

#aqui termina el ejercicio 3

#------------------------------------------------------------------

#Ejercicio 4
from clases.ejercicio4 import sensorYmediciones


if __name__ == "__main__":
    # Crear un sensor
    sensor_temperatura = Sensor("Sensor de Temperatura")

    # Registrar algunas mediciones
    sensor_temperatura.registrar_medicion(23.5)
    sensor_temperatura.registrar_medicion(25.2)
    sensor_temperatura.registrar_medicion(22.8)
    sensor_temperatura.registrar_medicion(26.1)

    # Mostrar el resumen del sensor
    sensor_temperatura.mostrar_resumen()

#aqui termina ejercicio 4

#--------------------------------------------------------------------



#ejercicio 5 pelicula y catalogo


from clases.ejercicio5 import Pelicula, Catalogo

if __name__ == "__main__":
    # Crear un catálogo
    catalogo = Catalogo()

    # Registrar películas
    catalogo.registrar_pelicula("Inception", "Ciencia Ficción", 2010)
    catalogo.registrar_pelicula("Titanic", "Romance", 1997)
    catalogo.registrar_pelicula("Interstellar", "Ciencia Ficción", 2014)
    catalogo.registrar_pelicula("Gladiator", "Acción", 2000)

    # Mostrar catálogo completo
    catalogo.mostrar_catalogo()

    # Buscar una película existente
    catalogo.buscar_pelicula("Titanic")

    # Buscar una película que no existe
    catalogo.buscar_pelicula("Avatar")

    # Filtrar películas por género
    catalogo.filtrar_por_genero("Ciencia Ficción")

    # Filtrar un género inexistente
    catalogo.filtrar_por_genero("Comedia")

    # Mostrar el catálogo actualizado
    catalogo.mostrar_catalogo()
#Fin ejercicio 5

#---------------------------------------------------------

#Ejercicio 6 usuarioAutenticacion
from clases.ejercicio6 import usuarioYautenticacion

if __name__ == "__main__":
        sistema = SistemaAutenticacion()
        sistema.menu()
    
#fin ejercicio 6

#------------------------------------------------------------


#Ejercicio 7 
        from clases.ejercicio7 import agendaYcontacto

        #if __name__ == "__main__":
        agenda = Agenda()

        while True:
                print("\n MENÚ AGENDA \n")
                print("1 Agregar nuevo contacto")
                print("2 Mostrar todos los contactos")
                print("3 Buscar contacto por nombre")
                print("4 Eliminar contacto")
                print("5 Salir")

                opcion = input("Seleccione una opción (1-5): ")

                if opcion == "1":
                   nombre = input("Nombre: ")
                   telefono = input("Teléfono: ")
                   correo = input("Correo electrónico: ")
                   agenda.agregar_contacto(nombre, telefono, correo)

                elif opcion == "2":
                        agenda.mostrar_contactos()

                elif opcion == "3":
                        nombre = input("Ingrese el nombre del contacto a buscar: ")
                        agenda.buscar_contacto(nombre)

                elif opcion == "4":
                        nombre = input("Ingrese el nombre del contacto a eliminar: ")
                        agenda.eliminar_contacto(nombre)

                elif opcion == "5":
                 print("Saliendo del sistema de agenda. ¡Hasta luego!")
                 break

                else:
                 print(" Opción no válida. Intente nuevamente")