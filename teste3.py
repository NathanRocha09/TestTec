{
    "faturamento_diario": [
        {"dia": "2024-01-01", "valor": 100.0},
        {"dia": "2024-01-02", "valor": 150.0},
        {"dia": "2024-01-03", "valor": 0.0},
        {"dia": "2024-01-04", "valor": 200.0},
        {"dia": "2024-01-05", "valor": 0.0},
        {"dia": "2024-01-06", "valor": 50.0},
        {"dia": "2024-01-07", "valor": 300.0},
    ]
}


import json

def processar_faturamento(json_file):
    # Carregar os dados do arquivo JSON
    with open(json_file, 'r') as file:
        dados = json.load(file)
    
    faturamentos = [item['valor'] for item in dados['faturamento_diario'] if item['valor'] > 0]
    
    if not faturamentos:
        print("Não há faturamento válido para processamento.")
        return
    
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    
    media_mensal = sum(faturamentos) / len(faturamentos)
    
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)
    
    print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

# Substitua 'faturamento.json' pelo caminho do seu arquivo JSON
processar_faturamento('faturamento.json') 