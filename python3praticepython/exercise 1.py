nome = input("Qual seu nome?")
idade = int(input("Qual sua idade?"))
# cem_anos = 100 - idade
# cem_anos = 2019 + cem_anos
repetir_mensagem = int(input("Quantas vezes quer ver esta mensagem ?"))
cem_anos = str((2019 - idade)+100)
print(("Seu nome é {} e sua idade atual é {}. O ano em que vai fazer 100 anos é {}\n".format(nome,idade, cem_anos)) * repetir_mensagem)

# 100 - idade e o resultado somar com idade
#duas formas de resolver o mesmo problema, sendo a não comentada transformando a formula em string e jogando dentro da variavel cem_anos.