class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def cambiar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)

if __name__ == "__main__":
    persona1 = Persona("Dante", 17, "Masculino")
    persona1.mostrar_informacion()

    print("\nCambiando edad...\n")
    persona1.cambiar_edad(30)
    persona1.mostrar_informacion()

        
