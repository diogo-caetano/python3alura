# import random
#
# t1 = str(input('Nome do primeiro trabalho: '))
# t2 = str(input('Nome do segundo trabalho: '))
# t3 = str(input('Nome do terceiro trabalho: '))
# t4 = str(input('Nome do quarto trabalho: '))
#
# lista = [t1, t2, t3, t4]
#
# print('A ordem em que os trabalhos serão apresentados é: \n{}'.format(random.sample(lista, 4)))
# o codigo acima funciona também, perfeitamente. Porém o codigo a rodar é a segunda solução pro mesmo problema.


from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)