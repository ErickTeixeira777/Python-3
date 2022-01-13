#simples e compostas, simples com if composta com else
'''nome = str(input('Qual é seu nome? '))
if nome == 'Erick':
    print('Que nome lindo!')
else:
    print('Seu nome é legal!' )     
print('Bom dia, {}!'.format(nome))'''
n1 = float(input('Digite a 1° nota:'))
n2 = float(input('Digite a 2° nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f} '.format(m))
print('PARABÉNS VC É FODA!😀' if m >=6 else 'BURRÃO EM FI! 🐴')    