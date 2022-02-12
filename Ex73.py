''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão na ordem de colocação, depois monstre:
A)Os 5 primeiros
B)Os últimos 4 colocados
C)Times em ordem alfabéticas
D)Em que posição estáo time do Santos '''

times = ('America - MG','Athletico Paranaense - PR','Atlético - GO','Atlético Mineiro - MG','Avaí - SC','Botafogo - RJ','Ceará - CE','Corinthians - SP','Coritiba - PR','Cuiabá - MT','Flamengo - RJ','Fluminense - RJ','Fortaleza - CE','Goiás - GO','Internacional - RS','Juventude - RS','Palmeiras - SP','Bragantino - SP','Santos - SP','São Paulo - SP')
#print(f'Lista de times: {times}')
print('-='*15)
for t in times:
    print(t)
print('-='*15)  
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)  
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)  
print(f'Times por ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Santos está na {times.index("Santos - SP")+1}° posição! ')