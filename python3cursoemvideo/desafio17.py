import math

catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjascente : '))

print('O comprimento da hipotenusa é de {}'.format(math.hypot(catop, catad)))