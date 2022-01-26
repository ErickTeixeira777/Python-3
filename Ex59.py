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
print('\033[4;36;40m{:=^30}\033[m'.format('Code-Save'))
n1 = int(input('\033[4;36;40mDigite o 1° valor:\033[m '))
n2 = int(input('\033[4;36;40mDigite o 2° valor:\033[m '))
opção = 0
sleep(1)
while opção !=5:
    print('''\033[4;36;40mEscolha uma opção:      
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novo Valor
[5]EXIT\033[m''')
    opção = int(input('\033[4;36;40mEscolha uma opção:\033[m '))
    if opção == 1:
       somar = n1 + n2 
       print('\033[4;36;40mA soma entre os valores é {}\033[m '.format(somar))
    elif opção == 2:
       multiplicar = n1 * n2
       print('\033[4;36;40mA multiplicação entre os valores é {} \033[m'.format(multiplicar))
    elif opção == 3:
       if  n1 > n2:
         maior = n1
       else:
         maior = n2  
       print('\033[4;36;40mO maior valor digitado foi {}\033[m '.format(maior))
    elif opção == 4:
       print('\033[4;36;40mInforme os valores novamente\033[m')
       n1 = int(input('\033[4;36;40mDigite o 1° valor:\033[m '))
       n2 = int(input('\033[4;36;40mDigite o 2° valor:\033[m '))
    elif opção == 5:
       print('\033[4;36;40mFinalizando...\033[m ')
    else:
        print('\033[4;36;40mOpção invalidade!\033[m ')
    print('\033[4;36;40m=-=\033[m'*10)   
    sleep(1)                 
print('\033[4;36;40mFim do programa! Volte sempre! \033[m')
