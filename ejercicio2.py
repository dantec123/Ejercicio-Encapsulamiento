class persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre=nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self,edad):
        self.edad=edad
        
    def get_sexo(self):
        return self.sexo
    
    def set_sexo(self,sexo):
        self.sexo=sexo
    
    def cambiar_edad(self):
        
    
if __name__=="__main__":
    persona1=persona("Gabriel",17,"Masculino")
    print(persona1.mostrar_info())
        
