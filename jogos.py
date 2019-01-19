import forca
import advinhacao

print("********************************")
print("**********Bem vindo !!**********")
print("********************************")

print("Escolha o jogo que quer jogar")
print("[1] - Forca , [2] - Adivinhação")
jogo = int(input("Jogo escolhido:"))

if(jogo == 1):
    print("Forca !")
    forca.forca()
elif(jogo == 2):
    print("Adivinhação!")
    advinhacao.advinhação()


print("Fim do jogo!")       