# Aula 1 PLN
#EXE1
a = input("Qual o teu nome? ")
b = a.upper()
print(b)

#EXE2
lst = []
n = int(input("Comprimento da lista de numeros : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print("Lista é ",lst)

lista_pares = [x for x in lst if x%2==0]
print("Os valores pares da lista são ", lista_pares)

#EXE3
# introduzir o caminho do ficheiro .txt
ficheiro = input("Introduza o ficheiro: ")

# abrir o ficheiro em modo de leitura(read)
with open(ficheiro, "r") as f:

    # ler todas as linhas do ficheiro numa lista
    linhas = f.readlines()

    # inverter a lista
    linhas.reverse()

    # iterar sobre a lista invertida e imprimir cada linha
    print("Linhas inversas do ficheiro: ")
    for l in linhas:
        print(l.strip())

#EXE4
import string

nome = input("Introduza o ficheiro: ")
with open(nome, 'r') as n:
    texto = n.read()

#remover pontuação convert to lowercase
texto = texto.translate(str.maketrans('', '', string.punctuation))
texto = texto.lower()

# traduzir o texto numa lista de palavras
palavras = texto.split()

# contar as ocorrencias de cada palavra
conta_palavras = {}
for palavra in palavras:
    if palavra in conta_palavras:
        conta_palavras[palavra] += 1
    else:
        conta_palavras[palavra] = 1

# ordenar o dicionário por valor em ordem decrescente
ordena_palavras = sorted(conta_palavras.items(), key=lambda x: x[1], reverse=True)

# imprimir as 10 palavras mais frequentes e as suas ocorrencias
for palavra, contar in ordena_palavras[:10]:
    print(f"{palavra}: {contar}")

#EXE5

import string
from unidecode import unidecode

def clean_text(texto):
    # remover espaços em brancos
    texto = texto.strip()

    # remover pontuação convert to lowercase
    texto = texto.translate(str.maketrans('', '', string.punctuation))

    #converter para minusculas
    texto = texto.lower()

    # remover acentuação
    texto = unidecode(texto)

    return texto

print("Exercicio 5 propoe limpar uma frase. A frase inicial é  OLAAAAA, isto é um texto exemplo !, a frase limpa = ", clean_text("OLAAAAA, isto é um texto exemplo !"))


#NOVO SLIDE:
#EXE1

rev = input("Introduza uma frase para inverter: ")
print("frase invertida: ", rev[::-1])


#EXE2

def conta_a(string):
    return string.count('a')

def conta_A(string):
    return string.count('A')

f = "Hey, eu sou a ANA Carolina. E tu quem és???"
print("Na frase 'Hey, eu sou a ANA Carolina. E tu quem és???' existem ", conta_a(f), " a's e ", conta_A(f), " A's.")


#EXE3

def conta_vogal(string):
    count = 0
    vogal = "aeiouAEIOU"
    for char in string:
        if char in vogal:
            count += 1
    return count

print("Na frase Este semestre vai ser interessante existem ",conta_vogal("Este semestre vai ser interessante."), " vogais.")


#EXE4

l = input("Introduza uma frase: ")
print("Agora em minusculas = ", l.lower())

#EXE5

m = input("Introduza uma frase: ")
print("Agora em maiusculas = ",m.upper())