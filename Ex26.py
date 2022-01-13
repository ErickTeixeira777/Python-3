# Primeira e última ocorrência de uma string 
# Faça um programa que leia uma frase pelo teclado e mostre: 
# Em que posição ela aparece a primeira e última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('Aletra A aparece {} vezes na frase. '.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A útima letra A apareceu na posição {}'.format(frase.rfind('A')+1))