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
print(lst)

lista_pares = [x for x in lst if x%2==0]
print(lista_pares)

#EXE3
# introduzir o caminho do ficheiro .txt
#Caminho: /Users/anacarolinaalves/Desktop/plne/TPC1/plneb.txt
file = input("Introduza o ficheiro: ")

# abrir o ficheiro em modo de leitura(read)
with open(file, "r") as file:

    # ler todas as linhas do ficheiro numa lista
    lines = file.readlines()

    # inverter a lista
    lines.reverse()

    # iterar sobre a lista invertida e imprimir cada linha
    for line in lines:
        print(line.strip())

#EXE4
import string

filename = input("Introduza o ficheiro: ")
with open(filename, 'r') as file:
    text = file.read()

#remover pontuação convert to lowercase
text = text.translate(str.maketrans('', '', string.punctuation))
text = text.lower()

# traduzir o texto numa lista de palavras
words = text.split()

# contar as ocorrencias de cada palavra
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# ordenar o dicionário por valor em ordem decrescente
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# imprimir as 10 palavras mais frequentes e as suas ocorrencias
for word, count in sorted_words[:10]:
    print(f"{word}: {count}")

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

print("Exercicio 4 propoe limpar uma frase. A frase inicial é  OLAAAAA, isto é um texto exemplo !, a frase limpa = ", clean_text("OLAAAAA, isto é um texto exemplo !"))


#NOVO SLIDE:
#EXE1

rev = input("Introduza uma frase: ")
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