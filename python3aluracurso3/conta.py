class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print ("Construindo objeto ... {}".format(self))
        self.__numero     = numero
        self.__titular    = titular
        self.__saldo      = saldo
        self.__limite     = limite

    def extrato(self):
        print("O saldo do {} é de {} ".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @@property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


#
# from conta import Conta
#
# input("Qual conta quer ver ?")
#
# if input("1"):
#     conta = Conta(123, "Diogo", 100.0, 1000.0)
#     print(conta.titular)
#     conta.extrato()
# elif("2"):
#     conta2 = Conta(321, "Maria", 1000.0, 10000.0)
#     print(conta.titular)
#     conta.extrato()
