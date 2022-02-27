'''Crie um programador que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores inpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas'''
val = list()
ímpares = list()
pares = list()
while True:
    val.append(int(input('Digite um valor: ')))
    r = str(input('Gostaria de continuar? [S/N] ')) 
    if r in 'Nn':
        break
for i, v in enumerate(val):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('='*30)
val.sort()
print(f'A lista completa é {val} ')
print(f'A lista de pares é {pares} ')
print(f'A lista de ímpares é {ímpares} ')

