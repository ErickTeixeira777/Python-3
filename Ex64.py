'''Crie um programa que leia vários números inteiros 
pelo teclado, o programa só vai parar quando o usuário
digitar o valor 777, que é a condição de parada
No final mostre quantos números foram digitados 
e qual foi a soma entre eles 
(desconsiderando o flag). '''
print('{:=^37}'.format('Code-Save'))
print('{:=^37}'.format('No Flags'))
núm = cont = soma = 0
núm = int(input('Digite [777] para finalizar: '))
while núm != 777:
    soma += núm
    cont += 1
    núm = int(input('Digite [777] para finalizar: '))
print('Você digitou {} números e a soma entre eles foi {} '.format(cont , soma))        