print("********************************")
print("Bem vindo no jogo de advinhação!")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu número:")

print("Você digitou" , chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print("Você acertou")
else:
    if (maior):
        print("Você errou, o seu chute foi maior do que o número secreto.")
    elif (menor):
        print("Você errou, o seu chute foi menor do que o número secreto.")


print("Fim do jogo!")       