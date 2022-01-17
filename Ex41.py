'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER'''
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do Atleta: '))
idade = atual - nasc 
print('Você tem {} anos! '.format(idade))
if idade <= 9:
    print('Atleta MIRIM! ')
elif idade <= 14:
    print('Atleta INFANTIL! ')  
elif idade <=19:
    print('Atleta JUNIOR! ')
else:
    print('Atleta MASTER! ')    



