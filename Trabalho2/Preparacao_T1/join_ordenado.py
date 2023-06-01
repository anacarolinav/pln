import json

with open('in_join_t1.json', encoding='utf-8') as file:
    data = json.load(file)

for key, value in data.items():
    descricao = value.get('descricao', '')
    designacao = value.get('designacao', '')

    if descricao and designacao:
        descricao_completa = f"{descricao} {designacao}"
        data[key]['descricao'] = descricao_completa

    elif designacao:
        data[key]['descricao'] = designacao

    else:
        data[key]['descricao'] = descricao

    # Verificar se a chave 'descricao' existe antes de removê-la
    if 'designacao' in data[key]:
        del data[key]['designacao']

# Remover a chave 'designacao' se for uma string vazia
for key, value in data.items():
    if value['descricao'] == "":
        del value['descricao']

# Ordenar as chaves em ordem alfabética
ordered_data = dict(sorted(data.items()))

with open('out_join_t1.json', 'w', encoding='utf-8') as file:
    json.dump(ordered_data, file, indent=4, ensure_ascii=False)