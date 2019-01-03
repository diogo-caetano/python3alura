idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
criança     = idade < 12
adolescente = idade >= 12

if(maior_idade):
    print("Você é maior de idade!")
elif(criança):
    print("Você é uma criança!")
else:
    print("Você é um adolescente!")