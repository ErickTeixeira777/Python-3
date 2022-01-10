# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
c = float(input('Informe a temperatura em °C:' ))
# f ((9 * c) / 5) + 32 >>> nesse caso os parênteses são dispensáveis pelo fato da soma estar na ordem de correta de precedência
f =  9 * c  / 5 + 32
print('A temperatura de {} °C corresponde a  {} °F!' .format(c, f))