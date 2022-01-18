'''Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:

À vista dinheiro: 10% Off
À vista débito: 5% Off
Em 2x preço normal
3x ou mais no crédito: 20% de juros'''
print('{:=^40}'.format(' Lojas Code-Save '))
preço = float(input('Digite o preço do produto:'))
print('''Formas de pagamento
[1]à vista dinheiro
[2]à vista débito
[3]2x no cartão
[4]3x ou mais no cartão''')
opção = int(input('Escolha uma opção: '))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção ==3:
    total = preço 
    parcela = total / 2
    print('Parcelada em 2x: de {:.2f} '.format(parcela))  
elif opção == 4:
    total = preço + (preço * 20/100)      
    totparc = int(input('Em quantas x?')) 
    parcela = total / totparc
    print('Parcelar em {}x de {:.2f} com juros'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA')    
print('Valor final da compra R${:.2f}'.format(total, preço))    

