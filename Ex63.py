'''Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os 10 primeiros elementos de uma 
sequência de fibonacci.
Ex: 0>1>1>2>3>5>8>13'''
print('{:=^37}'.format('Code-Save'))
print('{:=^37}'.format('Sequência de Fibonacci'))
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('='*37)
print('{} >> {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('>> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM DA SEQUÊNCIA!')


