'''Crie um programa que leia o nome e o preço de vários produtos
O programa deverá perguntar se o usuário quer continuar 
No final mostre
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de 1k.
C) Qual é o nome do produto mais barato.'''
print('\033[36m{:=^37}\033[m'.format('Code-Save'))
print('\033[31m{:=^37}\033[m'.format('Eletro-Tex'))
total = tot1k = menor = cont = 0
barato = ' '
while True:
    produto = str(input('\033[36mNome do produto:\033[m '))
    preço = float(input('Preço do produto R$: '))
    cont += 1
    total += preço
    if preço > 1000:
        tot1k += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
         resp = str(input('\033[36mContinuar compra [S/N]?\033[m ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[36m{:=^37}\033[m'.format('Obrigado, Volte sempre')) 
print(f'O total da compra foi R$:{total:.2f} ')
print(f'\033[36m{tot1k} produtos custaram mais de 1k!\033[m ')
print(f'O produto mais barato foi o(a):{barato}, que custou R$:{menor:.2f}! ')

