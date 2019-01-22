# numero = int(input("Qual número deseja verificar ?"))
# if(numero % 4 == 0):
#     print("O número é par e divisível por 4.")
# elif(numero % 2 == 0):
#     print("O número é par.")
# else:
#     print("O número é impar.")

# programa no comentário exibe se o número é divisível por 4 ou se é só par ou impar. Funcionando.

num = int(input("Qual o primeiro número?"))
check = int(input("Qual o segundo número?"))
if(check % num == 0):
    print("Os números são divisíveis e o resto e zero.")
else:
    print("Os números são fracionados.")