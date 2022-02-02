#simples e compostas, simples com if composta com else
'''nome = str(input('Qual é seu nome? '))
if nome == 'Erick':
    print('Que nome lindo!')
else:
    print('Seu nome é legal!' )     
print('Bom dia, {}!'.format(nome))'''

'''print('{:=^37}'.format('Code-Save'))
print('{:=^37}'.format('Calcule sua Média'))
n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
média = (n1 + n2)/2
print('A sua média foi {:.1f} '.format(média))
if média >= 6.0:
   print('PARABÉNS VC É FODA!😀' )
else:
   print('\033[0;30;47mBURRÃO EM FI!\033[m 🐴'   )'''

print('{:=^37}'.format('Code-Save'))
c1 = float(input('Números de quartos da 1° Casa: '))
c2 = float(input('Númeors de quartos da 2° Casa: '))   
m = (c1 + c2) / 2
print('A média de quartos foi {:.1f} '.format(m))
if m > 7.0:
    print('Essa seria uma boa compra!😀 ')
else:
    print('Continue procurando novos impreendimentos!')     



 