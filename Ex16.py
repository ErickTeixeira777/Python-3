# Quebrando um número
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira! ex: Digite um número: 6.127 O número 6.127 tem a parte Inteira 6.

# import math
from math import trunc
num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e sua porção inteira é {}' .format(num, math.trunc(num)))
print('O valor digitado foi {} e sua porção inteira é {}' .format(num, trunc(num)))
