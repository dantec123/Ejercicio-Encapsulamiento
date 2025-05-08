from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def descripcion(self):
        return f"'{self.titulo}' de {self.autor}  escrito en {self.año_publicacion}."

    def es_clasico(self):
        año_actual = datetime.now().year
        return (año_actual - self.año_publicacion) > 50

if __name__ == "__main__":
    libro = Libro("Chac Mool", "Carlos Fuentes", 1954)
    print(libro.descripcion())

    if (libro.es_clasico()):
        print("Este libro es un clásico.")
    else:
        print("Este libro no es un clásico.")
