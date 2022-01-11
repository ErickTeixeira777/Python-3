'''Um professor quer sortear um dos seus alunos para apagar o quadro, Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido'''
from random import choice
n1 = input('1° aluno:')
n2 = input('2° aluno:')
n3 = input('3° aluno:')
n4 = input('4° aluno:')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}' .format(escolhido))
