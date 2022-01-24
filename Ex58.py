'''Faça um programa que melhore o jogo do desafio 28
onde o computador vai pensar em um número de 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar
mostrando no final quantos palpites foram necessários
para vencer'''
from random import randint
from time import sleep
computador = randint(0,10)
sleep(3)
print('🎲' * 20)
print('Tente adivinhar um número entre 0 e 10 ')
print('Adivinhe-me se for capaz! ')
print('🎲' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador < computador:
        print('Tente um número maior!')
    if jogador > computador:
        print('Tente um número menor! ')    
    elif jogador == computador:
          acertou = True
sleep(1)  
print('🎲' * 20) 
print('🎯 PARABÉNS!🎯 ')
print('✨Acertou miseraviii✨ ')
print('✨Você precisou {} palpites!✨ '.format(palpites))
print('🎲' * 20)


      
