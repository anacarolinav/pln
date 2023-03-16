import re

#TPC: percorrer o livro doenças digestivo e a cada palavra que encontrar e está no dicionario-medico, faz <a link=DESCRICAO > TERMO </a>
#Fim é ter um ficheiro html (?)


file_livro = open('/Users/anacarolinaalves/Desktop/MESTRADO/2/PLN/1603/TPC4/LIVRO-Doenças-do-Aparelho-Digestivo.txt', 'r', encoding="utf-8")
text_livro = file_livro.read()

# Separa o livro em paragrafos
paragraphs = text_livro.split('\n\n')


#abrir o dicionario-medico
file_dict = open('/Users/anacarolinaalves/Desktop/MESTRADO/2/PLN/1603/dicionario_medico.xml', 'r', encoding="utf-8")
text_dict = file_dict.read()

def limpa(text):
    #lembrar que \s apanha \n tab e muitos espaços
    text = re.sub(r"\s+"," ",text)
    #tira os \n no inicio e no fim
    return text.strip()

#1º retirar os </page>
remove_f = re.sub(r"</?page.*>","", text_dict)

#2º retirar os <text> (acrescentamos ao .* um ? para parar no 1º >)
remove_text = re.sub(r"</?text.*?>","", remove_f)

#3º extrair termos(1ºgrupo captura) e explicação(2ºgrupo de captura)
extract_terms_expl = re.findall(r"<b>(.*)</b>([^<]*)",remove_text)

#4º listar tuplos na forma (termo, limpa(explicações))
extract_terms_expl = [(term, limpa(expl)) for term, expl in extract_terms_expl]

#5º converter lista de tuplos para dicionario: (grangrena, morte de tecidos por falta de irrigação de sangue)
dicionario = dict(extract_terms_expl)





#abrir o livro digestivo.html para ler 
#percorrer o livro e procurar as palavras do dicionario.keys()
with open("livro-digestivo3.html",'w', encoding='utf-8') as livro:
    livro.write('<html>\n<head>\n</head>\n<body>\n')

    for paragraph in paragraphs:
        words = paragraph.split()
        for i, word in enumerate(words):
            word_stripped = word.strip(".,?!-()\"'")
            if word_stripped.lower() in dicionario:
                link = f'<a href="{dicionario[word_stripped.lower()]}">{word_stripped}</a>'
                words[i] = link

        paragraph = " ".join(words)
        livro.write("<p>" + paragraph + "</p>\n")

    livro.write('</body>\n</html>')
    livro.close()

with open("livro-digestivo3.html",'r', encoding='utf-8') as livro2:
    html_content = livro2.read()

print(html_content)


file_livro.close()
file_dict.close()
livro2.close()
