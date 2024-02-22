
valores_faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(valores_faturamento.values())

print("Representação de cada estado em relação ao faturamento total:")
for estado, faturamento in valores_faturamento.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")