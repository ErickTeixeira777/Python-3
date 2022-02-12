''' Crie um programa que vai gerar 5 números aleatórios e colocar em um tupla, depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. '''
from random import randint
numeros = (randint (1,10), randint (1,10), randint (1,10), randint (1,10), randint (1,10))
print('Os números sorteados foram: ')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi o: {max(numeros)}! ')   
print(f'O Menor número sorteado foi o: {min(numeros)}! ') 