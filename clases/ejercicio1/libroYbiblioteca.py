#clases libro biblioteca 

class Libro:
    def __init__(self,titulo,autor,copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        if self.copias > 0:
           self.copias -=1
           print(f"Se ha prestado el libro '{self.titulo}'.")
        else: 
            print(f"No hay copias disponbles de '{self.titulo}'.")
           
    def devolver(self):
        self.copias +=1
        print(f"se ha devuelto el libro'{self.titulo}'.")

    def mostrar_estado(self):
        print(f"Titulo:{self.titulo}|Autor:{self.autor}|Copias disponibles:{self.copias}")



class Biblioteca:
    def __init__(self):
        self.catalogo={}

    def registrar_libro(self, titulo, autor, copias):
        if titulo in self.catalogo:
            print(f"El libro'{titulo}'Ya esta registrado")
        else:
            self.catalogo[titulo]=Libro(titulo, autor, copias)
            print(f"Libro'{titulo}'registradocon exito.")

    def mostrar_catalogo(self):
            if not self.catalogo:
                print("No hay libros registrados en la biblioteca")
            else: 
                print("Catalogo Completo:")
                for libro in self.catalogo.values():
                    libro.mostrar_estado()
                    
    def buscar_libro(self, titulo):
        if titulo in self.catalogo:
            print(f"Libro encontrado:")
            self.catalogo[titulo].mostrar_estado()
        else:
            print(f"El libro'{titulo}'no se encuentra en la biblioteca")
        
    def prestar_libro(self, titulo):
        if titulo in self.catalogo:
            self.catalogo[titulo].prestar()
        else:
            print(f"El libro '{titulo}'no esta en el catalogo")

    def devolver_libro(self, titulo):
        if titulo in self.catalogo:
            self.catalogo[titulo].devolver()
        else:
            print(f"El libro'{titulo}'no esta en el catalogo")