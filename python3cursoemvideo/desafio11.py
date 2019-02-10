largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A área total é de {}m2, sendo necessários assim {} litros de tinta'.format(area, tinta))
