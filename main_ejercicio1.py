#Main Ejercicio1 libro y biblioteca con menu incluido 


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
                print(" Opción no válida. Intentelo de nuevo ")