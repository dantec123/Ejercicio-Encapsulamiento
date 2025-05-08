class CuentaBancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    def depositar(self, cantidad):
        if (cantidad > 0):
            self.saldo += cantidad
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if (cantidad <= self.saldo):
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes. No se puede realizar el retiro.")

    def mostrar_informacion(self):
        print("Titular:", self.titular)
        print("Número de cuenta:", self.numero_cuenta)
        print("Saldo actual:", self.saldo)

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Dante Corzo", 1000, "102030501")
    cuenta1.mostrar_informacion()

    print("+ $500...")
    cuenta1.depositar(500)
    cuenta1.mostrar_informacion()

    print(" -$2000...")
    cuenta1.retirar(2000) 
    cuenta1.mostrar_informacion()

    print("-$700...")
    cuenta1.retirar(700)
    cuenta1.mostrar_informacion()
