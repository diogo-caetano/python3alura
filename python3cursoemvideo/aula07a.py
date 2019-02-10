n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s   = n1 + n2
m   = n1 * n2
d   = n1 / n2
di  = n1 // n2
e   = n1 ** n2

print('A soma e:{} , \no produto é:{}, \na divisão é:{:.3f}, \na divisão inteira é:{}, \ne a exponênciação é:{}'.format(s, m, d, di, e))