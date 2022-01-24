'''Refaça o Ex51, lendo o primeiro termo e a razão de uma
P.A mostrando os 10 primeiros termos da programação usando
a estrutura while.'''
''' resolução do EX51 utilizando FOR 
print('TERMOS DE P.A')
primeiro = int(input('1° Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
   print('{}'.format(c), end=' > ') 
print('ACABOU!!!')'''
print('{:=^30}'.format('Code-Save'))
print('{:=^30}'.format('Gerador de PA'))
primeiro = int(input('1° Termo: '))
razão = int(input('Razão PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}>>>>'.format(termo), end='')
    termo += razão
    cont += 1
print('Fim!')    


