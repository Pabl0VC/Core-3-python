class CuentaBancaria:
    def __init__(self,  tipo_cuenta, tasa_interés, balance=0,): 
        self.tipo_cuenta = tipo_cuenta
        self.tasa_interés = tasa_interés
        self.balance = balance



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
        print(f"Balance ${self.balance}\n")
        return self


    def generar_interés(self):
        print (f"Tipo de cuenta:{self.tipo_cuenta} \nCon una tasa de interés de {self.tasa_interés}:")
        self.balance= self.balance + (self.tasa_interés)*(self.balance)
        # self.mostrar_info_cuenta() 
        # print("\t")
        return self


Cuenta_Corriente = CuentaBancaria("Cuenta Corriente", 0.1, 100)
Cuenta_Ahorro = CuentaBancaria("Cuenta Ahorro",0.2)


Cuenta_Corriente.depósito(100).depósito(100).depósito(300).retiro(50).generar_interés().mostrar_info_cuenta()
Cuenta_Ahorro.depósito(1000).depósito(600).retiro(100).retiro(100).retiro(100).retiro(100).generar_interés().mostrar_info_cuenta()
