'''Melhore o Ex61 perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa se encerra quando ele disser que 
quer mostrar 0 termos.'''
print('{:=^30}'.format('Code-Save'))
print('{:=^30}'.format('Gerador de PA'))
primeiro = int(input('1° Termo: '))
razão = int(input('Razão PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}>>>>'.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA!')
    mais = int(input('gostaria de analisar mais algum termo: '))   
print('Progressão finalizada com {} termos' .format(total))  
