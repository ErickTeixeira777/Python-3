# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'SANTO'.
cid = str(input('Em que cidade você mora: ')).strip()
print(cid[:5].upper() == 'SANTO')