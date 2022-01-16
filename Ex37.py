'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual seráa base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: \n[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {} '.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oct(num))) 
elif opção == 3:
    print('{} converido para HEXADECIMAL é igual a {} '.format(num, hex(num)))     
else:
    print('Opção inválida !!!')      
