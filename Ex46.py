'''Estrutura de laços de controle
Crie um programa que leia em contagem regressiva,
para uma queima de fogos de artifício, 
com uma pausa de 1sec entre os números'''
print('-=-'*10)
print('Fogos da Virada')
print('-=-'*10)
from time import sleep 
for c in range(10, -1, -1):
    print(c,)
    print('-=-'*10)
    sleep(1)
print('!!!HAPPY NEW YEAR!!!') 
print('-=-'*10)     

