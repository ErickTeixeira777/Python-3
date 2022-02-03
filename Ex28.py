'''Escrevam um programa que faça o computador ''pensar'' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
computador = randint(1, 10) #faz o computador "pensar"
print('🎲' * 20)
print('Vou pensar em um número entre 1 a 10.\nTente adivinhar...')
print('🎲' * 20)
jogador = int(input('Em que número eu pensei? '))
print('🎲' * 20)# jogador tenta adivinhar
sleep(5)
if jogador == computador:
    print('🎯 PARABÉNS!🎯 Acertou miseraviii')
else:
    print('✨ GANHEI TROUXAAA, CHUPAAA!!!✨ \nEu pensei no número {} e não no {}!'.format(computador, jogador))