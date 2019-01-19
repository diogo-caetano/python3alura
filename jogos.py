import forca
import advinhacao
def escolhe_jogo():
    print("********************************")
    print("**********Bem vindo !!**********")
    print("********************************")

    print("Escolha o jogo que quer jogar")
    print("[1] - Forca , [2] - Adivinhação")
    jogo = int(input("Jogo escolhido:"))

    if(jogo == 1):
        print("Forca !")
        forca.jogar()
    elif(jogo == 2):
        print("Adivinhação!")
        advinhacao.jogar()


    print("Fim do jogo!")
if (__name__ == "__main__"):
    escolhe_jogo()      