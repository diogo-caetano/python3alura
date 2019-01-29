class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self, dia, mes, ano):
        print("A data formatada é {} / {} / {}".format(self.dia, self.mes, self.ano))


from datas import Data
d = Data(21, 11, 2007)
d.formatada(21, 11, 2007)
