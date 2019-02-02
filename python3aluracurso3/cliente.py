class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando o @property nome ()")
        return self.__nome.title()


    @nome.setter
    def nome(self, nome):
        print("Chamando o setter nome ()")
        self.__nome = nome