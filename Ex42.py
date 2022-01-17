'''Refaça o Ex35 dos trângulos, acresentando o recurso de mostar que tipo de triângulo será formado:

Equilátero: todos os lados iguais:
Isósceles: dois lados iguais:
Escaleno: todos os lados diferentes'''
r1 = float(input('1° Seguimento: '))
r2 = float(input('2° Seguimento: '))
r3 = float(input('3° Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('Os seguementos acima podem formar "TRIÂNGULO"!', end=' ')
    if r1 == r2 == r3:
        print('"EQUILÁTERO"')
    elif  r1 != r2 != r3 != r1:
        print('"ESCALENO"')     
    else:
        print('"ISÓSCELES"')    
