'''Condições Aninhadas'''
print('\033[36m{:=^37}\033[m'.format('Code-Save'))
print('\033[31m{:=^37}\033[m'.format('Condições'))
nome = str(input('Qual é seu nome? '))
if nome == 'Erick':
    print('Que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')    
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')    
else:
    print('Seu nome é bem normal.')    
print('Tenha um bom dia, {}!'.format(nome))

