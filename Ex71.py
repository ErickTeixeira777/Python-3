'''Crie um programa que simule o funcionamento de um caixa eletrônico
No início pergunte ao usuário qual será o valor a ser sacado
eo o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de 100,50,20,10,02 R$ '''
print('='*30)
print('\033[36m{:^32}'.format('Code-Bank\033[m'))
print('='*30)
valor = float(input('Qual valor quer sacar? R$'))
total = valor
céd = 50
totcéd = 0 
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd >0:
           print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10: 
            céd = 2
        totcéd = 0    
        if total == 0:
            break    
print('='*35)
print('\033[36mCode-Bank agradece sua preferência!\033[m ')               
print('='*35)
