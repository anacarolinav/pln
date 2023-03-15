
# 3 capture group -> \n\n(.+)((\n.+)+) 
    #1 (.+)  para termos
    #2 (\n.+) para as descrições 
    #3 ((\n.+)+) para a descrição total mas marcamos este com ?: para o silenciar, ou seja, nao o guarda


import re

file=open('/Users/anacarolinaalves/Desktop/MESTRADO/2/PLN/aula0903/dicionario_medico.txt', encoding= "utf-8")
text = file.read()

#remove (1 sequencia pode conter novas linhas que começa apos \n\n\f e termina antes de \n\n) 
#adicionar \n + 1ºgrupo de captura (.+\n\n) = todas as linhas de texto ate a ultima linha que contem 2 \n consecutivos (fim de paragrafo) 
remove_n_f_n = re.sub(r"\n\n\f(.+\n\n)", r"\n\1", text)

#captura e retira sequencia que começa apos \n\n\f e termina com uma letra [(?:) --> significa que este grupo de captura não deve ser considerado na contagem]
#vai adicionar neste local \n\n + 1º grupo de captura ((?:.+)\n[A-ZÁÀÉÚÍÓÂÃÕ]) = \n seguido de um conjunto de caracteres. Util para capturar bloco de texto
remove_f_string = re.sub(r"\n\n\f((?:.+)\n[A-ZÁÀÉÚÍÓÂÃÕ])", r"\n\n\1", remove_n_f_n)

#substitui a sequencia \n\n\f por apenas 1 \n, ou seja, remove o caracter de form-feed e une os paragrafos num unico texto
remove_f_2n = re.sub(r"\n\n\f", r"\n", remove_f_string)

#substitui o form-feed (\f) por uma string vazia
remove_f = re.sub(r"\f","",remove_f_2n)


#identificamos os termos/Designações
mark_terms = re.sub(r"\n\n(.+)", r"\n\n#T=\1", remove_f)

#identificamos as explicações/Descrições
mark_explications = re.sub(r"\n([^#\s].+)", r"\n#E=\1", mark_terms)

#identifica a sequencia: termo \n\n termo como uma explicação
correct_explications = re.sub(r"(#T=.+)\n\n#T=(.+)", r"\1\n#E=\2", mark_explications)

#substitui o \n que poderá existir entre 2 explicações por um espaço.
remove_new_lines = re.sub(r"(#E=.+)(?:\n#E=(.+))+", r"\1 \2", correct_explications)

#substitui as marcas de identificação por vazio -> junta termo e explicação
remove_marks = re.sub(r"#[TE]=", r"", remove_new_lines)

#retorna uma lista de tuplos na forma (termo, explicação)
new_entries = re.findall(r"\n\n(.+)\n(.+)", remove_marks)


file.close()


html=open("dicionario_medico.html",'w', encoding='utf-8')

header = '''
<html>
<head>
<meta charset='utf-8'/>
<title> Dicionário Médico </title>
</head>
<body style="background-color:white;">
<h1 style="text-align:center;"> <br> Welcome to my medical dictionary! </h1>           
<p style="text-align:center;">This file is organized by designation and the description on the side. <br></p> 

'''

lista=list(new_entries)
lista.insert(0,("Designation", "Description"))

# Create the HTML table
table = "<table style='border: 1px solid black;border-collapse: collapse;'>\n"
for i, row in enumerate(lista):
    table += "<tr>"
    for j, item in enumerate(row):
        if i == 0: 
            table += "<th style='font-weight:bold; border: 1px solid black;border-collapse: collapse;background-color: #4169e1;';>{}</th>".format(item)
        else:
            table += "<td style='border: 1px solid black;border-collapse: collapse;'>{}</td>".format(item)
    table += "</tr>\n"
table += "</table>"


footer = '''
<p style="text-align:left;">This file  was designed by Ana Carolina Veloso. <br></p> 

</body>
</html>
'''

html.write(header+table+footer)


html.close()
