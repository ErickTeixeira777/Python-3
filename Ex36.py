'''Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da parcela mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
print('===== Code-Save  Financiamentos ===== ')
print('=' * 37)
casa = float(input('Digite o valor da casa! '))
print('=' * 37)
salário = float(input('Salário do comprador: R$ '))
print('=' * 37)
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('=' * 37)
print('Para pagar uma casa de R${:.3f} \nEm {} anos!!! '.format(casa, anos))
print('=' * 37)
print('A prestação será de R${:.3f} '.format(prestação))
print('=' * 37)
if prestação <= mínimo:
    print('Parabéns financiamento Aprovado!!!')
else:
    print('Sinto muito financiamento Negado!!!')
print('=' * 37)    
