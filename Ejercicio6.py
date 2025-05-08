class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

if __name__ == "__main__":
    rectangulo = Rectangulo(20, 10)
    print("Área del rectángulo:", rectangulo.calcular_area())
    print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())
