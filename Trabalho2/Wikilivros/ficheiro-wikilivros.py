import requests

from bs4 import BeautifulSoup
import json

url="https://pt.wikibooks.org/wiki/Dicionário_de_termos_médicos"
url2 = "https://pt.wikibooks.org/wiki/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

div_link = soup.find_all("table", class_="toc noprint")
#print(div_link)

urls = []
for div in div_link:
    print(div)
    for link in div.find_all("a", href=True):
        urls.append(url2 + link["title"])

#print("\n\n".join(urls))


lista_term=[]
lista_output=[]

for u in urls:
    html_ = requests.get(u).text
    soup_ = BeautifulSoup(html_, "html.parser")
    divs = soup_.find_all("div", class_="mw-parser-output")
    #print("AIAI",divs)

    for div in divs:
        #dá as doenças em caixas
        doenca = div.find_all("p")
        for p in doenca:
            termo = p.find_all("b")
            for t in termo:
                title = t.text.strip(":")
                desc = p.text.strip(": ").replace(t.text, "").strip()
                descricao = desc.replace(":", "")
                lista_output.append({title: {"desc": descricao}})


#file = open("wikilivros.json", "w")
#json.dump(lista_output, file, ensure_ascii=False, indent=4)
#file.close()

