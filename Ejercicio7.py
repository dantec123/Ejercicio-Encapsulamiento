class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def aumentar_salario(self, porcentaje):
        if (porcentaje > 0):
            aumento = self.salario * (porcentaje / 100)
            self.salario += aumento
        else:
            print("El porcentaje debe ser mayor a cero.")

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Departamento:", self.departamento)
        print("Salario actual:", round(self.salario, 2))

if __name__ == "__main__":
    empleado1 = Empleado("Dante Corzo", 1000, "Ventas")
    empleado1.mostrar_informacion()

    print("Salario aumentado un 10%")
    empleado1.aumentar_salario(10)
    empleado1.mostrar_informacion()
