class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def agregar_nota(self, nota):
        if (0 <= nota <= 10):
            self.notas.append(nota)
        else:
            print("La nota debe estar entre 0 y 10.")

    def calcular_promedio(self):
        if (len(self.notas) > 0):
            return sum(self.notas) / len(self.notas)
        else:
            return 0

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Notas:", self.notas)
        print("Promedio:", self.calcular_promedio())

if __name__ == "__main__":
    estudiante1 = Estudiante("Dante Corzo", 17)
    estudiante1.agregar_nota(5)
    estudiante1.agregar_nota(9)
    estudiante1.agregar_nota(7)

    estudiante1.mostrar_info()
