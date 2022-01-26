'''Faça um programa que jogue par ou impar
O jogo será interrompido quando o jogador PERDER
mostrando o total de vitórias consecutivas que 
ele conquistou no final do jogo'''
from random import randint
v = 0
while True:
    print('='*40)    
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]    
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu! ')
            v += 1 
        else:
            print('Você Perdeu! ')
            break    
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu! ')
            v += 1
        else:
            print('Você Perdeu! ')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes. ')            
print('='*40)










'''número =int(input('Digite um número qualquer: '))
resultado = número % 2 
if resultado ==0:
    print('O número {} é ==PAR== '.format(número))
else:
    print('O número {} é ==IMPAR== '.format(número)) '''