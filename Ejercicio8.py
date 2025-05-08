class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aumentar_stock(self, cantidad):
        if (cantidad > 0):
            self.stock += cantidad
        else:
            print("La cantidad debe ser mayor que cero.")

    def disminuir_stock(self, cantidad):
        if (cantidad > 0):
            if (self.stock - cantidad >= 0):
                self.stock -= cantidad
            else:
                print("No hay suficiente stock para realizar esta operación.")
        else:
            print("La cantidad debe ser mayor que cero.")

    def mostrar_informacion(self):
        print("Producto:", self.nombre)
        print("Precio:", self.precio)
        print("Stock:", self.stock)

if __name__ == "__main__":
    producto1 = Producto("naranja", 100, 20)
    producto1.mostrar_informacion()

    print("Aumentando el stock a 10 unidades:")

    producto1.aumentar_stock(10)
    producto1.mostrar_informacion()

    print("Disminuyendo el stock en 40 unidades:")
    
    producto1.disminuir_stock(40)
    producto1.mostrar_informacion()
