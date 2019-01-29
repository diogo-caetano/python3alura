class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print ("Construindo objeto ... {}".format(self))
        self.numero     = numero
        self.titular    = titular
        self.saldo      = saldo
        self.limite     = limite

    def extrato(self):
        print("O saldo do {} é de {} ".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


from conta import Conta

input("Qual conta quer ver ?")

if input("1"):
    conta = Conta(123, "Diogo", 100.0, 1000.0)
    print(conta.titular)
    conta.extrato()
elif("2"):
    conta2 = Conta(321, "Maria", 1000.0, 10000.0)
    print(conta.titular)
    conta.extrato()
