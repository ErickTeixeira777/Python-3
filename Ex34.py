'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salário superiores a R$1.200,00\nCalcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%. '''

salário = float(input('Qual é o salário do funcionário?'))
if salário <= 1300:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print('Quem ganhava R${:.3f} passa a ganhar R${:.3f} agora.'.format(salário, novo))        