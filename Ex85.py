'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''
núm = [[], []]
valor = 0
for c in range (1, 8):
    valor = int(input(f'Digite o {c}°. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor) 
print('-='*30)
print(f'Os valores pares foram: {núm[0]} ')
print(f'Os valores ímpares foram: {núm[1]} ')           
  