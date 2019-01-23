# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for element in a:
#     if(element < 5):
#         print(element)
#  exercício feito

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for element in a:
#     if(element < 5):
#         new_list = element
#         print(new_list)
#desafio 1 completo

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

numero_escolhido = int(input("Qual o número?"))

for numero in a:
    if numero <= numero_escolhido:
        print(numero)

