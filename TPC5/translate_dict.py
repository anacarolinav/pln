#TPC = o mesmo que na aula mas usar como google tradutor o ficheiro termos_traduzidos.txt

def translate_text(text, target_lang='en'):
    with open('/Users/anacarolinaalves/Documents/GitHub/pln/TPC5/termos_traduzidos.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    translations = {}
    for line in lines:
        key, value = line.strip().split(' @ ')
        translations[key] = value
    try:
        return translations[text]
    except KeyError:
        #print(f'Term "{text}" not found in translations.')
        return text


import json
file_in = open("/Users/anacarolinaalves/Documents/GitHub/pln/TPC4/dicionario_medico.json","r",encoding="utf-8")
dici = json.load(file_in)

new_dici = {}

#key=designation
#value=description
for key, value in dici.items():
    en_translation = translate_text(key, 'en')
    new_dici[key] = {
                    "description": value,
                    "en" : en_translation
                    }

file_out = open("/Users/anacarolinaalves/Documents/GitHub/pln/TPC5/dicionario_translate_resultado.json","w",encoding="utf-8")
json.dump(new_dici, file_out,ensure_ascii=False, indent=4)

file_in.close()
file_out.close()
