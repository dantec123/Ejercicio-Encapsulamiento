class CuentaBancaria:
    def __init__(self, numero_cuenta):
        self.__saldo = 0.0  
        self.__numero_cuenta = numero_cuenta  

    def depositar(self, cantidad):
        """Método para depositar dinero en la cuenta."""
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad} en la cuenta {self.__numero_cuenta}.")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta {self.__numero_cuenta}.")
        else:
            print("La cantidad a retirar debe ser mayor que 0 y no puede exceder el saldo disponible.")

    def get_saldo(self):
        return self.__saldo


if __name__ == "__main__":
    cuenta = CuentaBancaria("123456789")

    print(f"Saldo inicial: {cuenta.get_saldo()}")

    cuenta.depositar(1000.0)
    print(f"Saldo después del depósito: {cuenta.get_saldo()}")

    cuenta.retirar(200.0)
    print(f"Saldo después del retiro: {cuenta.get_saldo()}")

    cuenta.retirar(900.0)
    print(f"Saldo después del intento de retiro: {cuenta.get_saldo()}")

    cuenta.depositar(-50.0)
    print(f"Saldo después del intento de depósito negativo: {cuenta.get_saldo()}")
