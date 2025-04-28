class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"

if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", 2020)
    print(coche1.mostrar_informacion())
