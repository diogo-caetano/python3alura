class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print ("Construindo objeto ... {}".format(self))
        self.__numero       = numero
        self.__titular      = titular
        self.__saldo        = saldo
        self.__limite       = limite

    def extrato(self):
        print("O saldo do {} é de {} ".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel


    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else
            print("O valor {} passou o limite.".format(valor))

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

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco': '237'}

#print("Qualquer coisa")

def melquisedeque(self):
    return self.print("viadão")

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
