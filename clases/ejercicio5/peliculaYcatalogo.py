# Ejercicio 5 — Película, Catálogo y Metodo Menu


class Pelicula:
    def __init__(self, titulo, genero, anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio

    def __str__(self):
        return f"{self.titulo} ({self.anio}) - Género: {self.genero}"


class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        print(f" Película '{pelicula.titulo}' agregada al catálogo.")

    def mostrar_catalogo(self):
        if self.peliculas:
            print("\n Catálogo de Películas:")
            for i, pelicula in enumerate(self.peliculas, start=1):
                print(f"{i}. {pelicula}")
        else:
            print("\n El catálogo está vacío.")

    def buscar_por_titulo(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                print(f" Película encontrada: {pelicula}")
                return
        print(f" No se encontró ninguna película con el título '{titulo}'.")

    def filtrar_por_genero(self, genero):
        filtradas = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        if filtradas:
            print(f"\n Películas del género '{genero}':")
            for p in filtradas:
                print(p)
        else:
            print(f" No hay películas del género '{genero}'.")

#______________Metodo Menu________
def menu():
    print("\n    SISTEMA DE CATÁLOGO DE PELÍCULAS    \n")
    print("1- Agregar nueva película")
    print("2- Mostrar catálogo completo")
    print("3- Buscar película por título")
    print("4- Filtrar películas por género")
    print("5- Salir del Menu")
    return input("\n Seleccione una opción: ")