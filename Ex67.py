'''Faça um programa que mostre a tabuada
de vários números , um de cada vez
para cada valor digitado pelo usuário
o programa será interrompido quando o número
solicitado for negativo'''
print('{:=^51}'.format('Code-Save'))
print('{:=^51}'.format('Tabuada'))
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('='*40)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('='*40)  
print('Programa Encerrado!') 
print('='*40)        
'''num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
        print('{} x {} = {}'.format(num, c, num*c))'''
