'''Desenvolva um programa que leia 
o nome, idade e sexo de quatro pessoa.
E no final mostre a média de idade do grupo
o nome do homem mais velho do grupo e quantas
mulheres têm menos de 20 anos.'''
somaidade = 0
médiaidade = 0 
maioridadehomem = 0
nomevelho = ' '
nomevelha = ' '
totmulher20 = 0
for p in range(1, 5):
    print('----{}° Pessoa----' .format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade 
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome   
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1 
        nomevelha = nome  
médiaidade  = somaidade / 4
print('A média de ideade do grupo é de  {} anos' .format(médiaidade))   
print('O homem mais velho do grupo tem {} anos e seu nome é {}! '.format(maioridadehomem, nomevelho)) 
print('Ao todo são {} mulheres com menos de 20 anos!\nNo grupo, e a mulher mais velha do grupo é a {}!'.format(totmulher20, nomevelha))


    