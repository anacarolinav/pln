from bs4 import BeautifulSoup
import json
import requests

url = "https://beduka.com/blog/materias/biologia/sistemas-do-corpo-humano"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

orgaos = {}
parar = False

elementos_h3 = soup.find_all("h3")

for i, elemento in enumerate(elementos_h3):
    strong_element = elemento.find("strong")
    if strong_element:
        orgaos_texto = strong_element.text.strip()
        orgaos[orgaos_texto] = {}

        next_sibling = elemento.next_sibling
        
        if next_sibling and next_sibling.name == "p":
            orgao_descricao += next_sibling.text.strip()
            orgaos[orgaos_texto][orgaos_texto] = orgao_descricao
            
            next_sibling = next_sibling.next_sibling

            if next_sibling.name == "h3":
                parar = True
                break
            
            elif next_sibling.name == "h4":
                orgao_nome = next_sibling.find("strong").text.strip()
                orgao_descricao = ""
                orgao_siblings = next_sibling.find_next_siblings()
                for orgao_sibling in orgao_siblings:
                    if orgao_sibling.name == "h4" or orgao_sibling.name == "h3" or orgao_sibling.name == "h2":
                        break
                    elif orgao_sibling.name == "p":
                        orgao_descricao += orgao_sibling.text.strip() + " "
                orgaos[orgaos_texto][orgao_nome] = orgao_descricao.strip()
                
            elif next_sibling.name == "h5":
                orgao_nome = next_sibling.find("strong").text.strip()
                orgao_descricao = ""
                orgao_siblings = next_sibling.find_next_siblings()
                for orgao_sibling in orgao_siblings:
                    if orgao_sibling.name == "h4" or orgao_sibling.name == "h3" or orgao_sibling.name == "h2":
                        break
                    elif orgao_sibling.name == "p":
                        orgao_descricao += orgao_sibling.text.strip() + " "
                    elif orgao_sibling.name == "ul":
                        orgao_descricao += orgao_sibling.text.strip() + " "
                orgaos[orgaos_texto][orgao_nome] = orgao_descricao.strip()
                

        else:
            while next_sibling:
                if next_sibling.name == "h3":
                    parar = True
                    break
                elif next_sibling.name == "h4":
                    orgao_nome = next_sibling.find("strong").text.strip()
                    orgao_descricao = ""
                    orgao_siblings = next_sibling.find_next_siblings()
                    for orgao_sibling in orgao_siblings:
                        if orgao_sibling.name == "h4" or orgao_sibling.name == "h3" or orgao_sibling.name == "h2":
                            break
                        elif orgao_sibling.name == "p":
                            orgao_descricao += orgao_sibling.text.strip() + " "
                    orgaos[orgaos_texto][orgao_nome] = orgao_descricao.strip()
                elif next_sibling.name == "h5":
                    orgao_nome = next_sibling.find("strong").text.strip()
                    orgao_descricao = ""
                    orgao_siblings = next_sibling.find_next_siblings()
                    for orgao_sibling in orgao_siblings:
                        if orgao_sibling.name == "h4" or orgao_sibling.name == "h3" or orgao_sibling.name == "h2":
                            break
                        elif orgao_sibling.name == "p":
                            orgao_descricao += orgao_sibling.text.strip() + " "
                        elif orgao_sibling.name == "ul":
                            orgao_descricao += orgao_sibling.text.strip() + " "
                    orgaos[orgaos_texto][orgao_nome] = orgao_descricao.strip()
                
                next_sibling = next_sibling.next_sibling

# Convertendo os dados para formato JSON
json_data = json.dumps(orgaos, ensure_ascii=False, indent=4)

# Salvando os dados em um arquivo JSON
with open("sistemas.json", "w", encoding="utf-8") as file:
    file.write(json_data)
