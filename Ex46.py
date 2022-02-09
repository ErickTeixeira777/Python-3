'''Estrutura de laços de controle
Crie um programa que leia em contagem regressiva,
para uma queima de fogos de artifício, 
com uma pausa de 1sec entre os números'''
print('\033[32m-=-'*6)
print('!Fogos da Virada!')
print('-=-'*6)
from time import sleep 
for c in range(10, -1, -1):
    sleep(2)
    print(c,)
    print('-=-'*2)
    sleep(1)
print('\033[32m!\033[31m!!H \033[34mA \033[35mP \033[36mP \033[32mY *\033[31m N \033[34mE \033[35mW * \033[32m Y \033[36mE \033[31mA \033[34mR \033[35m! \033[32m! !\033[ \033[m') 
print('-=-'*13)     

