'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

Média abaixo de 5.0:
REPROVADO

Média entre 5.0 e 6.9:
RECUPERAÇÃO

Média 7.0 ou superior:
APROVADO'''
n1 = float(input('Qual é sua 1° nota: '))
n2 = float(input('Qual é sua 2° nota: '))
m = (n1 + n2) / 2
print('média {}'.format(m))
if m < 5.0:
    print('Reprovado! '.format(m))
elif m == 5.0 or 6.9:
    print('Recuperação! '.format(m))
elif m > 7.0:
    print('Aprovado! '.format(m))        
