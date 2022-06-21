import json

with open("faturamentoMensal.json") as dados:
    faturamento_mensal = json.load(dados)

total = 0
for i in faturamento_mensal:
    total += i['valor']

for i in faturamento_mensal:
    percentual = (i['valor'] * 100) / total 
    print(f"Percentual de {i['estado']} foi de {percentual:.2f}")