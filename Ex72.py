'''Crie um programa que tenha uma "tupla" totalmente preenchida com uma contagem por extenso, de 0 até 20.
Seu programa deverá ler um número pelo teclado (entre  0 e 20) e mostralá - lo por extenso.'''

cont = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True: 
    núm = int(input('Digite um número entre 0 e  20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente! ')   
print(f'Você digitou o número {cont[núm]} !') 

        
