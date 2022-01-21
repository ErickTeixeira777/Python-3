'''Desenvolva um programa que leia o 
primero termo ea razão de uma PA.
No final ,mostre os 10 primeiros termos dessa progressão.'''
print('TERMOS DE P.A')
primeiro = int(input('1° Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
   print('{}'.format(c), end=' > ') 
print('ACABOU!!!')   