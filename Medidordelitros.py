# Quantos litros de aguá vc vai ser preciso para encher uma piscina de x metros!
ladoa = float(input('Digite o tamanho do lado a da piscina:'))
ladob = float(input('Digite o tamanho do lado b piscina:'))
prof = float(input('Digite a pronfundidade da piscina: '))

área = ladoa * ladob * prof
print('Sua piscina tem a dimensão de {} X {} X {}! \nE a sua área é de {}m³.' .format(ladoa, ladob, prof, área))
litros = área * 1
print('Para encher sua piscina! \nVocê precisará de {:.3f} Litros de água!' .format(litros))
