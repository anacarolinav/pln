import json

# Abrir o arquivo JSON com o encoding especificado
with open('/Users/aliciasoliveiraa/Desktop/Universidade/Mestrado/2SEM/5ProcessamentoLinguagemNatural/pln_aulastp/TrabalhoGrupo2/Carol/out_join_wiki_t1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Converter os termos para minúsculas
data_lower = {term.lower(): value for term, value in data.items()}

# Reordenar o dicionário
data_sorted = dict(sorted(data_lower.items()))

# Escrever o dicionário de saída em um novo arquivo JSON com o encoding especificado
with open('ordenado_wiki_t1.json', 'w', encoding='utf-8') as file:
    json.dump(data_sorted, file, indent=4, ensure_ascii=False)
