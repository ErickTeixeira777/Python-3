# Faça um programa que leia o nome completo de uma pessoa.
#mostrando em seguida o primeiro e o últimonome separadamente.
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
