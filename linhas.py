#Esse programa não muito útil vai gerar dois números aleatórios entre 1 e 9 e somar os dois, após somar, gera outros dois números aleatórios e soma os dois, repetindo o ciclo até chegar a um número de linhas X que o usuário escolhe:
import random
i = 0
z = int(input('Quantas linhas você quer de números somados aleatórios?: '))

while(i<z):
	x = random.randint(1,9)
	y = random.randint(1,9)
	print(x+y)
	i = i+1

