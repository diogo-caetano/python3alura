# import random
#
# aluno1 = input('Digite o nome do primeiro aluno:')
# aluno2 = input('Digite o nome do segundo aluno:')
# aluno3 = input('Digite o nome do terceiro aluno:')
# aluno4 = input('Digite o nome do quarto aluno:')
#
# print('Os alunos são \n1- {} \n2- {} \n3- {} \n4- {}'.format(aluno1, aluno2, aluno3, aluno4))
#
# print('E o aluno sorteado é o aluno número: {}'.format(random.randrange(1, 5)))
#

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))