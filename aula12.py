'''Condições Aninhadas'''
nome = str(input('Qual é seu nome? '))
if nome == 'Erick':
    print('\033[4;36;40mQue nome bonito!\033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')    
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')    
else:
    print('Seu nome é bem normal.')    
print('Tenha um bom dia, {}!'.format(nome))
