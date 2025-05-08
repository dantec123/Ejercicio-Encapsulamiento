class Juego:
    def __init__(self, nombre, genero, precio):
        self.nombre = nombre
        self.genero = genero
        self.precio = precio

    def mostrar_informacion(self):
        print("Juego:", self.nombre)
        print("Género:", self.genero)
        print("Precio:", self.precio)

    def esta_en_oferta(self, precio_oferta):
        return self.precio < precio_oferta

if __name__ == "__main__":
    juego1 = Juego("Call of Duty", "FPS", 59)
    juego1.mostrar_informacion()

    if juego1.esta_en_oferta(40):
        print("El juego está en oferta")
    else:
        print("El juego no está en oferta")


