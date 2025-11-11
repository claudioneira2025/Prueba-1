# Ejercicio 5 — Película y Catálogo

class Pelicula:
    def __init__(self, titulo, genero, año):
        "Define una película con su título, género y año de lanzamiento"
        self.titulo = titulo
        self.genero = genero
        self.año = año

    def datos_pelicula(self):
        """Devuelve una representación legible de la película."""
        return f"Título: {self.titulo} | Género: {self.genero} | Año: {self.año}"


class Catalogo:
    def __init__(self):
        """Crea un catálogo vacío de películas."""
        self.peliculas = []

    def registrar_pelicula(self, titulo, genero, año):
        """Registra una nueva película en el catálogo."""
        nueva_pelicula = Pelicula(titulo, genero, año)
        self.peliculas.append(nueva_pelicula)
        print(f" Película '{titulo}' registrada correctamente.\n")

    def mostrar_catalogo(self):
        """Muestra todas las películas registradas."""
        print("\n CATÁLOGO COMPLETO DE PELÍCULAS:")
        if not self.peliculas:
            print(" No hay películas registradas aún.\n")
        else:
            for i, pelicula in enumerate(self.peliculas, start=1):
                print(f"{i}. {pelicula}")
            print()  # Línea en blanco final

    def buscar_pelicula(self, titulo):
        """Busca una película por su título."""
        print(f"\n Buscando película con título: '{titulo}'")
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                print(" Película encontrada:")
                print(pelicula, "\n")
                return pelicula
        print(" No se encontró ninguna película con ese título.\n")
        return None

    def filtrar_por_genero(self, genero):
        """Filtra y muestra las películas por género."""
        print(f"\n Películas del género: '{genero}'")
        filtradas = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        if not filtradas:
            print(" No se encontraron películas de ese género.\n")
        else:
            for i, pelicula in enumerate(filtradas, start=1):
                print(f"{i}. {pelicula}")
            print()
        return filtradas


