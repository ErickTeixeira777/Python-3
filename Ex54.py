'''Crie um programa que leia o ano de nascimento 
de sete pessoas, e no final mostre quantas pessoas
ainda não atingiram a maior idade e quantas já são 
maiores de idade'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0 
for pess in range(1,8):
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc 
    if idade >= 21:
       totmaior += 1
    else:
       totmenor += 1
print('Ao todo tivemos {} pessoas MAIORES! '.format(totmaior))
print('Ao todo tivemos {} pessoas MENORES! '.format(totmenor))        