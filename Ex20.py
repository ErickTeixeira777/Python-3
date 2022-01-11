'''O mesmo professor do desafio anterior quer sortear a ordem de apresentações de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
from random import shuffle 
n1 = input('1° Aluno: ')
n2 = input('2° Aluno: ')
n3 = input('3° Aluno: ')
n4 = input('4° Aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)