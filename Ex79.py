'''Faça um programa que o usuário possa digitar vários valores e cadastre-os em uma lista. Caso o número já exista, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente '''
números = list()
while True:
    n = int(input('Enter a value: '))
    if n not in números:
        números.append(n) 
        print('Value added successfully...')
    else:
        print('Doubled value! Try another value...')    
    r = str(input('Want to continue? [Y/N] '))
    if r in 'Nn':
        break
    print('='*30)
    números.sort()
    print(f'You entered the values {números}')