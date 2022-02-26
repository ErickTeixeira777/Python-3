'''Crie um programa onde o usuário possa digitar cinco valores e cadastre-os em uma lista, já na posição correta de inserção "sem usar a função sort()".
No final, mostre a lista ordenada na tela.'''
lista = [] #lista vazia
for c in range (0, 5): #lendo 5 valores
    n = int(input('Digite um valor: ')) #entre com um valor.
    #Agora vamos descobrir a posição dos valores
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
        # se o número for o primeiro ou o útimo da lista podemos simplesmente utilizar a função append.
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1 

                #enquanto a posição do número for menor que o elemento len de lista: podemos verificar se o número é menor ou igual a lista na posição pos
            
print('-'*30)
print(f'Os valores digitados em ordem foram {lista} ')            

               


      