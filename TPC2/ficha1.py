import re

#Exercício 1.1
line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"
lines = [line1, line2, line3]

def ex1(lines):
    print("\nExercicio 1.1")
    for x in lines:
        if re.match("hello",x):
            print("A palavra hello aparece no inicio.")
        else:
            print("A palavra hello não aparece no inicio.")

ex1(lines)

#Exercício 1.2
def ex2(lines):
    print("\nExercicio 1.2")
    for x in lines:
        if re.search("hello",x):
            print("A palavra hello aparece.")
        else:
            print("A palavra hello não aparece.")

ex2(lines)


#Exercício 1.3
linha13 = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
def ex3(linha13):
    print("\nExercicio 1.3")
    print(re.findall(r'[Hh][Ee][Ll][Ll][Oo]',linha13))

ex3(linha13)

#Exercício 1.4
linha14 = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
def ex4(linha14):
    print("\nExercicio 1.4")
    print(re.sub(r'[Hh][Ee][Ll][Ll][Oo]','*YEP*',linha14))

ex4(linha14)

#Exercício 1.5
linha15 ="bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
def ex5(linha15):
    print("\nExercicio 1.5")
    print(re.split(r',',linha15))

ex5(linha15)

#Exercício 2
def palavra_magica(frase):
    print("\nExercício 2")
    if re.search(r'por favor[.!?]$',frase) :
        print("Bem educado")
    else:
        print("Mal educado")


palavra_magica("Posso ir à casa de banho, por favor?")
palavra_magica("Preciso de um favor.")

#Exercício 3
def narcissismo(string):
    print("\nExercício 3")
    contar_eu = string.count(r"eu")
    print("A palavra 'eu' aparece", contar_eu, "vezes na string.")


narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou.")

#Exercício 4
def troca_de_curso(linha4, novo_curso):
    print("\nExercício 4")
    print(re.sub(r'LEI',novo_curso,linha4))


troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", "BIOMEDICA")


#Exercício 5
def soma_string(linha5):
    print("\nExercício 5")
    numeros = linha5.split(",")
    soma = 0
    for num in numeros:
        soma += int(num)
    print("A soma dos números é:", soma)


soma_string("4,-6,2,3,8,-3,0,2,-5,1")


#Exercício 6

def pronomes():
    print("\nExercício 6")
    frase6 = input("Frase = ")
    pronome = r'\b(eu|tu|ele|ela|nós|vós|eles|elas)\b'

    pronomes_encontrados = re.findall(pronome, frase6.lower())

    print("Na frase introduzida existem os seguintes pronomes: ", pronomes_encontrados)

pronomes()

#Exercício 7

def variavel_valida():
    print("\nExercício 7")
    nome7 = input("Introduza um nome de variável: ")
    letra = r'^[a-zA-Z]'
    # verifica se a string contém apenas letras, números e underscores
    valido = r'^\w*$'

    # verificar se a string é um nome válido para uma variável
    if re.match(letra, nome7) and re.match(valido, nome7):
        print(nome7," é um nome válido")
    else:
        print(nome7," é um nome inválido")

variavel_valida()

#Exercício 8

def inteiros(frase8):
    print("\nExercício 8")
    # expressão regular para localizar os números inteiros
    numeros = r'[-]?\b\d+\b'

    inteiros_encontrados = re.findall(numeros, frase8)

    inteiros_convertidos = [(x) for x in inteiros_encontrados]

    print("Estes são os inteiros encontrados: ", inteiros_convertidos)

inteiros("6,8,0,238467,-4,-6")


#Exercício 9

def underscores(frase9):
    print("\nExercício 9")
    frase9 = frase9.replace(' ', '_')

    frase9 = re.sub('_+', '_', frase9)

    print(frase9)

underscores("O tempo perguntou pro tempo quanto tempo o tempo tem.O tempo respondeu pro tempo que o tempo tem tanto tempo quanto tempo o tempo tem.")

#Exercício 10
lista10 = [
    "4700-000",
    "1234-567",
    "8541-543",
    "4123-974",
    "9481-025"
]

def codigos_postais(lista_cp):
    print("\nExercício 10")
    pares_cp = []

    for cp in lista_cp:
        # dividir o código postal em duas partes usando o hífen como separador
        partes_cp = cp.split('-')
        pares_cp.append(partes_cp)

    print(pares_cp)

codigos_postais(lista10)





