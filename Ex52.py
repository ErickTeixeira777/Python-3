'''Faça um programa que leia um número
inteiro e diga se ele é ou não um número primo
(número primo = dividido por 1 ou por ele mesmo)'''
num = int(input('Digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m ', end='')
        tot += 1
    else:
        print('\033[m ', end='')
    print('{}'.format(c), end='')
print('\033[m\nO número {} foi divisível {} vezes!' .format(num, tot))    
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')    

