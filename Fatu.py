import json

with open('faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)

minimo = faturamento_diario[0]
maximo = faturamento_diario[0]

dias_com_faturamento = [faturamento != 0 for faturamento in faturamento_diario]

media = sum([faturamento for faturamento in faturamento_diario if faturamento != 0]) / sum(dias_com_faturamento)

dias_acima_da_media = sum([1 for faturamento in faturamento_diario if faturamento > media])

for faturamento in [faturamento for faturamento in faturamento_diario if faturamento != 0]:
    if faturamento < minimo:
        minimo = faturamento
    elif faturamento > maximo:
        maximo = faturamento

print("Menor valor de faturamento diário: R$ {:.2f}".format(minimo))
print("Maior valor de faturamento diário: R$ {:.2f}".format(maximo))
print("Número de dias com faturamento acima da média mensal: {}".format(dias_acima_da_media))
