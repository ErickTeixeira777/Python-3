salário = float(input('Qual é o salário do funcionário?'))
aumento = salário + (salário * 15/100)
print('O salário do funcionário de R${:.2f} \nCom reajuste de 15% passará a ser R${:.2f}' .format(salário, aumento))