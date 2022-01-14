'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
print('='*20)
print('Analisando Triânulos')
print('='*20)
r1 = float(input('1° Seguimento: '))
r2 = float(input('2° Seguimento: '))
r3 = float(input('3° Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('Os seguementos acima podem formar "TRIÂNGULO"! ')
else:
    print('Os seguimentos acima NÃO podem formar "TRIÂNGULO"')    

