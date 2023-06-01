import json
from deep_translator import GoogleTranslator

translated_alemao = GoogleTranslator(source='pt', target='de')
translated_italiano = GoogleTranslator(source='pt', target='it')
translated_ingles = GoogleTranslator(source='pt', target='en')
translated_espanhol = GoogleTranslator(source='pt', target='es')

with open('ordenado_wiki_t1.json', 'r') as f:
    resultado = json.load(f)

new_resultado = {}

for termo, info in resultado.items():
    new_info = info.copy()
    print(termo)

    if 'alemao' not in new_info:
        alemao_termo = translated_alemao.translate(termo)
        new_info['alemao'] = alemao_termo

    if 'italiano' not in new_info:
        italiano_termo = translated_italiano.translate(termo)
        new_info['italiano'] = italiano_termo

    if 'ingles' not in new_info:
        ingles_termo = translated_ingles.translate(termo)
        new_info['ingles'] = ingles_termo

    if 'espanhol' not in new_info:
        espanhol_termo = translated_espanhol.translate(termo)
        new_info['espanhol'] = espanhol_termo

    new_resultado[termo] = new_info

with open('ordenado_wikit1_traducoes.json', 'w') as f:
    json.dump(new_resultado, f, indent=4, ensure_ascii=False)
