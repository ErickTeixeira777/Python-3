'''Escreva um programa que leia o sexo de um pessoa
mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente
até ter um valor correto.'''
sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos!\nDigite o sexo novamente: ')).strip().upper()
print('Obrigado: sexo [{}] registrado com sucesso!'.format(sexo))      
       