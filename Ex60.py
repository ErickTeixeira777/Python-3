'''Faça um programa que leia um número
qualquer e mostre o seu fatorial.
Ex: 5!=5x4x3x2x1=120'''
'''Modo simplificado'''
'''from math import factorial
n = int(input('Digite um valor:'))
f = factorial(n)
print('O fatorial de {} é {} '.format(n, f))'''

n = int(input('Digite um valor: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))    