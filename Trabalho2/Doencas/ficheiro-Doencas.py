import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.mdsaude.com/doencas-a-z/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

div_link = soup.find_all("table")

urls = []
for div in div_link:
    rows = div.find_all("a")
    for row in rows:
        href = row.get("href")
        urls.append(url + href)

lista_output = []

for u in urls:
    print(u)
    html_ = requests.get(u).text
    soup_ = BeautifulSoup(html_, "html.parser")
    divs = soup_.find_all("div", class_="entry-content")

    for div in divs:
        uls = div.find_all("ul")
        for ul in uls:
            lis = ul.find_all("li")
            for li in lis:
                link_a = li.find("a")
                page_url = link_a["href"]
                termo = link_a.text
                

                page_html = requests.get(page_url).text
                page_soup = BeautifulSoup(page_html, "html.parser")
                info_div = page_soup.find("div", class_="entry-content")

                if info_div is not None:
                    # Extrair subtítulos, parágrafos e listas
                    h2_tags = info_div.find_all("h2")

                # Criar dicionário para armazenar subtítulos, parágrafos e listas
                disease_info = {}
                for i in range(len(h2_tags)-1):
                    h2 = h2_tags[i]
                    next_h2 = h2_tags[i+1]
                    content_tags = []

                    next_sibling = h2.next_sibling
                    while next_sibling and next_sibling.name != "h2":
                        if next_sibling.name in ["p", "ul"]:
                            content_tags.append(next_sibling)
                        next_sibling = next_sibling.next_sibling

                    content_text = [tag.text for tag in content_tags]
                    disease_info[h2.text] = content_text

                # Tratar o último h2 e os content_tags restantes
                last_h2 = h2_tags[-1]
                last_content_tags = []
                next_sibling = last_h2.next_sibling
                while next_sibling:
                    if next_sibling.name in ["p", "ul"]:
                        last_content_tags.append(next_sibling)
                    next_sibling = next_sibling.next_sibling

                last_content_text = [tag.text for tag in last_content_tags]
                disease_info[last_h2.text] = last_content_text

                lista_output.append({{termo: disease_info}})
                #print(lista_output)

                
file_path = "doencas-MDSaude.json"
with open(file_path, "w") as file:
    json.dump(lista_output, file, ensure_ascii=False, indent=4)
