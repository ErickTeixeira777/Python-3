'''Estrutura de repetição!'''
'''utilizando o while'''
print('\033[36m{:=^37}\033[m'.format('Code-Save'))
print('\033[31m{:=^37}\033[m'.format('Estrutura de Repetição'))
n = 1 
par = impar = 0
while n != 0 :
    n = int(input('Digite um valor: '))
    if n != 0:
      if n % 2 == 0:
           par += 1
      else :
           impar += 1
print('Você digitou {} números pares e {} números ímpares! '.format(par, impar))            


