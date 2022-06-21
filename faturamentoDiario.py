import json

with open("dados.json") as dados:
    dados_faturamento = json.load(dados)

def maiorValor(maior):
    maior = dados_faturamento[0]['valor']
    for valor in dados_faturamento:
        if(valor['valor'] >= maior):
            maior = valor['valor']
    return maior

def menorValor(menor):
    menor = dados_faturamento[0]['valor']
    for valor in dados_faturamento:
        if(valor['valor'] > 0 and valor['valor'] <= menor):
            menor = valor['valor']
    return menor

def media():
    dias = total = 0
    for valor in dados_faturamento:
        if(valor['valor'] != 0):
            dias += 1
        total += valor['valor']
    media = total / dias
    return media

def diasSuperiorMedia():
    media_mensal = media()
    dias = 0
    for valor in dados_faturamento:
        if valor['valor'] > media_mensal:
            dias += 1
    return dias
 
maior = menor = 0
maior = maiorValor(maior)
menor = menorValor(menor)
dias = diasSuperiorMedia()

print(f"Maior valor de faturamento no mês: {maior}\nMenor valor de faturamento no mês: {menor}\nDias em que o valor de faturamento foi superior à média mensal: {dias}")