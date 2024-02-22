import json

def calculo_estatisticas_faturamento(data_faturamento):
    faturamento_diario = [registro['valor'] for registro in data_faturamento]
    
    faturamento_sem_zeros = [valor for valor in faturamento_diario if valor != 0]
    
    menor_faturamento = min(faturamento_sem_zeros)
    maior_faturamento = max(faturamento_sem_zeros)
    
    media_mensal = sum(faturamento_sem_zeros) / len(faturamento_sem_zeros)
    
    dias_acima_da_media = sum(1 for valor in faturamento_sem_zeros if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open('dados.json', 'r') as file:
    data_faturamento = json.load(file)

menor, maior, acima_da_media = calculo_estatisticas_faturamento(data_faturamento)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média mensal: {acima_da_media}")