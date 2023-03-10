
# 3 capture group -> \n\n(.+)((\n.+)+) 
    #1 (.+)  para termos
    #2 (\n.+) para as descrições 
    #3 ((\n.+)+) para a descrição total mas marcamos este com ?: para o silenciar, ou seja, nao o guarda


import re

file=open('/Users/anacarolinaalves/Desktop/MESTRADO/2/PLN/aula0903/dicionario_medico.txt', encoding= "utf-8")
text = file.read()


remove_form_feed = re.sub(r"\f", "", text)
mark_terms = re.sub(r"\n\n(.+)", r"\n\n#T=\1", remove_form_feed)
mark_explications = re.sub(r"\n([^#\s].+)", r"\n#E=\1", mark_terms)
correct_explications = re.sub(r"(#T=.+)\n\n#T=(.+)", r"\1\n#E=\2", mark_explications)
remove_new_lines = re.sub(r"(#E=.+)(?:\n#E=(.+))+", r"\1 \2", correct_explications)
remove_marks = re.sub(r"#[TE]=", r"", remove_new_lines)

new_entries = re.findall(r"\n\n(.+)\n(.+)", remove_marks)


file.close()


html=open("dicionario_medico.html",'w', encoding='utf-8')

header = '''
<html>
<head>
<meta charset='utf-8'/>
<title> Dicionário Médico </title>
</head>
<body style="background-color:beige;">
<h1 style="text-align:center;"> <br> Welcome to my medical dictionary! </h1>           
<p style="text-align:center;">This file is organized by designation and the description on the side. <br></p> 

'''

lista=list(new_entries)
lista.insert(0,("Designation", "Description"))

# Create the HTML table
table = "<table border='1'>\n"
for i, row in enumerate(lista):
    table += "<tr>"
    for j, item in enumerate(row):
        if i == 0: 
            table += "<th style='font-weight:bold';>{}</th>".format(item)
        else:
            table += "<td>{}</td>".format(item)
    table += "</tr>\n"
table += "</table>"


footer = '''
<p style="text-align:left;">This file  was designed by Ana Carolina Veloso. <br></p> 

</body>
</html>
'''

html.write(header+table+footer)


html.close()
