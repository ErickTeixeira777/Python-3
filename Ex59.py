'''Crie um programa que leia dois valores 
e mostre um menu na tela:
[1]soma
[2]multiplicador
[3]maior
[4]novos números 
[5]sair do programa
Seu programa deverá realizar
a operação solicitada em cada caso.'''
from time import sleep
print('{:=^30}'.format('Code-Save'))
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
opção = 0
sleep(1)
while opção !=5:
    print('''Escolha uma opção:      
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novo Valor
[5]EXIT''')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
       somar = n1 + n2 
       print('A soma entre os valores é {} '.format(somar))
    elif opção == 2:
       multiplicar = n1 * n2
       print('A multiplicação entre os valores é {} '.format(multiplicar))
    elif opção == 3:
       if  n1 > n2:
         maior = n1
       else:
         maior = n2  
       print('O maior valor digitado foi {} '.format(maior))
    elif opção == 4:
       print('Informe os valores novamente')
       n1 = int(input('Digite o 1° valor: '))
       n2 = int(input('Digite o 2° valor: '))
    elif opção == 5:
       print('Finalizando... ')
    else:
        print('Opção invalidade! ')
    print('=-='*10)   
    sleep(1)                 
print('Fim do programa! Volte sempre! ')
