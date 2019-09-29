#Números de 1 a 9, a cada 15 segundos soma 2 dos números de 1 a 9 aleatoriamente escolhidos.
#Fazer printar apenas 10 linhas

import random
i=0
t = int(input('Escolha o menor número para seu dado: '))
h = int(input('Escolha agora o maior número para seu dado: '))
z = int(input('Escolha agora o menor número para o segundo dado, caso não queira o segundo dado, escreva 0: '))
f = int(input('Escolha agora o maior número para o segundo dado, caso não queira segundo dado, escreva 0: '))
print('Agora o programa vai rolar um número aleatório para cada um dos dois dados e somar o número de ambos: ')
x = random.randint(t,h)
print('Este é o valor resultante do primeiro dado: ',x,', aperte enter para ver o próximo!')
input()
y = random.randint(z,f)
print('Este é o valor do segundo dado: ',y,', aperte enter para que o programa some os dois resultados!: ',x,'+',y,'=')
input()
print(x+y)

