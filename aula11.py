#CORES NO TERMINAL
# Lista de cores
# Preto '\033[30m'
# Vermelho '\033[31m'
# Verde '\033[32m'
# Amarelo '\033[33m'
# Azul '\033[34m'
# Roxo '\033[35m'
# Azul Claro '\033[36m'

print('\033[36m{:=^37}\033[m'.format('Code-Save'))
print('\033[31m{:=^37}\033[m'.format('Cores'))
#nome = str(input('Digite seu nome: '))
nome = 'Erick Leandro Teixeira '
cores = {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7;30m','preto':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','roxo':'\033[35m','azul claro':'\033[36m'}
print('!!{}{}{}!!'.format(cores['azul claro'], nome, cores['limpa']))




