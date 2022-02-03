'''Crie um programa que leia a idade e o sexo de várias pessoas
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar.
No final mostre :
A) Quantas pessoas são maiores de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos.'''
from time import sleep
print('\033[36m{:=^37}\033[m'.format('Code-Save'))
print('\033[31m{:=^37}\033[m'.format('Data-Base'))
tot18 = toth = totm20 = 0
while True:
    idade = int(input('\033[36mDigite sua idade:\033[m'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[36mDigite seu sexo:\033[m ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1   

    continuar = ' '    
    while continuar not in 'SN':
        continuar = str(input('Continue?\033[36m[S/N]?\033[m ')).strip().upper()[0]
    if continuar == 'N':
        break
sleep(2)
print(f'\033[36mTotal de pessoas com mais de 18 anos: "{tot18}"!\033[m ') 
sleep(2)  
print(f'Ao todo temos "{toth}" homens cadastrados! ')   
sleep(2)
print(f'\033[36mE "{totm20}" mulheres com menos de 20 anos!\033[m ')  
sleep(1)
print('\033[36m{:=^37}\033[m'.format('!!!Code-Save!!!'))
        
    
