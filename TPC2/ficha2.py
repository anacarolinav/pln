import re

#Exercício 1
texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

def iso_8601(texto):
    print("\nExercício 1")
    datas = re.findall(r'(\d{2})/(\d{2})/(\d{4})', texto)

    datas_iso = []
    for x in datas:
        data_str = '/'.join(x)
        dia, mes, ano = re.match(r'(\d{2})/(\d{2})/(\d{4})', data_str).groups()
        data_iso = f'{ano}-{mes}-{dia}'

        datas_iso.append(data_iso)

    print("Datas presentes no texto no formato ISO 8601: ",datas_iso)

iso_8601(texto)

#Exercício 2
file_names = [
  "document.txt", # válido
  "file name.docx", # inválido
  "image_001.jpg", # válido
  "script.sh.txt", # válido
  "test_file.txt", # válido
  "file_name.", # inválido
  "my_resume.docx", # válido
  ".hidden-file.txt", # válido
  "important-file.text file", # inválido
  "file%name.jpg" # inválido
]

def valido_filename(file_names):
    print("\nExercício 2")

    pattern = r'^[\w\-.]+\.([a-zA-Z]{2,5})$'
    for names in file_names:
        if re.match(pattern, names):
            print(f"{names} é nome de ficheiro válido.")
        else:
            print(f"{names} é nome de ficheiro inválido.")


valido_filename(file_names)

#Exercício 2.1

def valido_filename_dicionario(file_names):
    print("\nExercício 2.1")

    nomes_validos = {}
    pattern = r'^[\w\-.]+\.([a-zA-Z]{2,5})$'
    for names in file_names:
        if re.match(pattern, names):
            extensao = names.split(".")[-1]
            # adiciona o nome de ficheiro ao dicionário de nomes válidos
            if extensao in nomes_validos:
                nomes_validos[extensao].append(names)
            else:
                nomes_validos[extensao] = [names]

    print(nomes_validos)

valido_filename_dicionario(file_names)


#Exercício 3
texto3 = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com 
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
dos professores Pedro Rangel Henriques e José João Antunes Guimarães Dias De Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""


def converte_nome(texto_fonte):
    print("\nExercício 3")
    return re.sub(r"([A-Z]\w+)\s?((?:[A-Z]\w+\s?|d[oae]s?\s?)*)\s([A-Z]\w+)", r"\3, \1", texto_fonte)

print(converte_nome(texto3))


#Exercício 4
lista4 = [
    "4700-000", # válido
    "9876543", # inválido
    "1234-567", # válido
    "8x41-5a3", # inválido
    "84234-12", # inválido
    "4583--321", # inválido
    "9481-025" # válido
]

def codigos_postais(codigos):
    print("\nExercício 4")
    pares = []
    for codigo in codigos:
        partes = codigo.split("-")
        if len(partes) == 2:
            pares.append((partes[0], partes[1]))
        else:
            meio = len(codigo) // 2
            pares.append((codigo[:meio], codigo[meio:]))

    print(pares)

codigos_postais(lista4)


#Exercício 5
abreviaturas = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "UC": "Unidade Curricular",
    "PL": "Processamento de Linguagens"
}

texto5 = "A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."


def expande_abreviacoes(texto):
    print("\nExercício 5")
    texto_expandido = re.sub(r"/abrev{(\w+)}", lambda match: abreviaturas.get(match.group(1)), texto)
    print(texto_expandido)

expande_abreviacoes(texto5)


#Exercício 6
matriculas = [
    "AA-AA-AA", # inválida
    "LR-RB-32", # válida
    "1234LX", # inválida
    "PL 22 23", # válida
    "ZZ-99-ZZ", # válida
    "54-tb-34", # inválida
    "12 34 56", # inválida
    "42-HA BQ" # válida, mas inválida com o requisito extra
]

def matricula_valida(matriculas):
    print("\nExercício 6")

    formato1 = r'^\d{2}[-\s][A-Z]{2}[-\s]\d{2}$'
    formato2 = r'^[A-Z]{2}[-\s][A-Z]{2}[-\s]\d{2}$'
    formato3 = r'^([A-Z]{2}\s\d{2}\s\d{2})$'
    formato4 = r'^([A-Z]{2}-\d{2}-[A-Z]{2})$'


    for matricula in matriculas:

        if re.match(formato1, matricula) or re.match(formato2, matricula) or re.match(formato3, matricula) or re.match(formato4, matricula):
            print("Matricula válida: ", matricula)

        else:
            print("Matricula inválida: ", matricula)

matricula_valida(matriculas)

#Exercício 7

texto7 = """Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA]. 
Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].
Ficaram muito confusos, pois não conseguiam identificar a função daquilo.
Seria para [VERBO INFINITIVO]? Tentaram perguntar a [NOME DE PESSOA FAMOSA], que também não sabia.
Desanimados, pegaram no objeto e deixaram-no no [NOME DE LOCAL MASCULINO] mais próximo. 
Talvez os [NOME PLURAL MASCULINO] de lá conseguissem encontrar alguma utilidade para aquilo."""


def mad_libs(texto):
    print("\nExercício 7")
    espacos = re.findall(r"\[([\w\s]+)\]", texto)
    for espaco in espacos:
        resposta = str(input(f"Introduza {espaco} "))
        texto = re.sub(r"\[[\w\s]+\]", resposta, texto, 1)
    return texto

print(mad_libs(texto7))

#Exercício 8

texto8 = "O gato gato laranja é é malandro e lindo lindo ."
texto81 = "Amar é sonhar, amar é viver, amar é curtir."
def remover_palavras_repetidas(text):
    print("\nExercício 8")
    palavras = text.split()
    unico = []

    for i in palavras:
        if i not in unico:
            unico.append(i)
    return ' '.join(unico)


print(remover_palavras_repetidas(texto8), '\n', remover_palavras_repetidas(texto81))




