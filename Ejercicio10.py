class Circulo:
    def __init__(self, radio):
        if (radio < 0):
            print("El radio no puede ser negativo.")
            self.radio = 0
        else:
            self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2  

    def calcular_circunferencia(self):
        return 2 * 3.14159 * self.radio  

    def mostrar_informacion(self):
        print("Radio del círculo:", self.radio)
        print("Área:", round(self.calcular_area(), 2))
        print("Circunferencia:", round(self.calcular_circunferencia(), 2))

if __name__ == "__main__":
    circulo1 = Circulo(3)
    circulo1.mostrar_informacion()

    circulo2 = Circulo(-3)
    circulo2.mostrar_informacion()
