#Main ejercicio 5

from clases.ejercicio5.peliculaYcatalogo import Pelicula, Catalogo, menu

catalogo = Catalogo()

while True:
    opcion = menu()

    if opcion == "1":
        titulo = input("Ingrese el título de la película: ")
        genero = input("Ingrese el género de la película: ")
        try:
            anio = int(input("Ingrese el año de lanzamiento: "))
        except ValueError:
            print(" El año debe ser un número entero válido.")
            continue
        pelicula = Pelicula(titulo, genero, anio)
        catalogo.agregar_pelicula(pelicula)

    elif opcion == "2":
        catalogo.mostrar_catalogo()

    elif opcion == "3":
        titulo = input("Ingrese el título de la película a buscar: ")
        catalogo.buscar_por_titulo(titulo)

    elif opcion == "4":
        genero = input("Ingrese el género para filtrar: ")
        catalogo.filtrar_por_genero(genero)

    elif opcion == "5":
        print(" Saliendo del sistema Peliculas y Catalogos")
        break

    else:
        print(" Opción no válida. Intentelo de nuevo ")