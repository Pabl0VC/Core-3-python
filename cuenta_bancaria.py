class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interés, balance=0): 
        self.tasa_interés = tasa_interés
        self.balance =balance 

    def depósito(self, monto):
        self.balance += monto

        return self


    def retiro(self, monto):
        if monto > self.balance:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= monto+5
        else:
            self.balance -= monto
        return self

    def mostrar_info_cuenta(self):
        print(f" Balance {self.balance}")
        return self


    def generar_interés(self,interes):
        # self.balance = self.balance*(1+interes)
        self.balace= self.balance + self.balance*interes
        self.mostrar_info_cuenta()
        return self


CuentaBancaria1 = CuentaBancaria("balance cuenta 1")
CuentaBancaria2 = CuentaBancaria("balance")
CuentaBancaria3 = CuentaBancaria("balans")

CuentaBancaria1.depósito(100).depósito(100).depósito(300).retiro(50).mostrar_info_cuenta().generar_interés(0.1) 
CuentaBancaria2.depósito(400).depósito(600).retiro(100).retiro(100).retiro(100).retiro(100).mostrar_info_cuenta().generar_interés(0.2)
CuentaBancaria3.depósito(80).retiro(100).mostrar_info_cuenta()  