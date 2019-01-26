class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print ("Construindo objeto ... {}".format(self))
        self.numero     = numero
        self.titular    = titular
        self.saldo      = saldo
        self.limite     = limite


from conta import Conta
conta = Conta(123, "Diogo", 100.0, 1000.0)
print(conta.titular)