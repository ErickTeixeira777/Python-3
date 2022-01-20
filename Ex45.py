'''Crie um programa que faça o computador jogar Jockenpô com você.'''
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
print('-='*20)
jogador = int(input('Qual é sua jogada?'))
print('-='*20)
print('      JO')
sleep(1)
print('             KEN')
sleep(1)
print('                   PO!!!')
sleep(2)
print('-='*20)
print('Computador escolheu {}! '.format(itens[computador]))
print('-='*20)
print('Você escolheu {}! '.format(itens[jogador]))
print('-='*20)
if computador == 0: 
    if jogador == 0:
       print('EMPATE')
    elif jogador == 1:
       print('PLAYER 1 WIN')
    elif jogador == 2:
       print('PLAYER 2 WIN')
    else:
        print('JOGADA INVÁLIDA!')             
elif computador == 1:
    if jogador == 0:
        print('PLAYER 2 WIN')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('PLAYER 1 WIN')
    else:
        print('JOGADA INVÁLIDA!')   
elif computador == 2:        
    if jogador == 0:
        print('PLAYER 1 WIN')
    elif jogador == 1:
        print('PLAYER 2 WIN')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')   



