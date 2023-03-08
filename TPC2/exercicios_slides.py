import re

#1
print("\nExercício 1")
string1 = "Ola timoteo"
padrao = "[t]"
print(re.findall(padrao,string1))

#2
print("\nExercício 2")
string2 = "Ola Tiago queres uma torrada de Tomate"
padrao = "[tT]"
print(re.findall(padrao,string2))

#3
print("\nExercício 3")
string3 = "Hello, world!"
padrao = r"[a-zA-Z]"
resultado = re.findall(padrao,string3)
print(resultado, len(resultado), "letras")

#4
print("\nExercício 4")
string4 = "5 de Novembro"
padrao = "\d"
print("A string contem o digito ", re.findall(padrao,string4))

#5
print("\nExercício 5")
string5 = "O preço do leite subiu 1.50€"
padrao = r"\d+(\.\d+)?"
resultado = re.findall(padrao,string5)
print("A string contem parte decimal = ",resultado)

#6
print("\nExercício 6")
string6 = "Comprei uma casa a 120 000€, que pechincha!!"
string66 = "AA"
padrao = r".{4,}"
print("String com mais de 3 caracteres de comprimento ",re.findall(padrao,string6))

#7
print("\nExercício 7")
string7 = "Olha viste a Maria? Ela ficou de me trazer morangos, melancias e melões."
string77 = "MAriaaaana Mota"
padrao = r"M(?!.*m)"
resultado = re.findall(padrao,string77)
print("Esta string só tem M e nao m ",resultado)

#8
print("\nExercício 8")
string8 = "Ana Carolina Veloso"
padrao = r"(\w).*\1"
print("A string contem exatamente 2 vezes repetidos os caracteres ", re.findall(padrao,string8))

#9
print("\nExercício 9")
string9 = "aaaaaaaa"
padrao = r"^(\w)\1+$"
print("A string contem exatamente 1 vez repetida ", re.findall(padrao,string9))

#10
print("\nExercício 10")
string10 = "3 pratos de trigo para {três} tigres tristes {comerem}."
padrao = r"{([^{}]*)}"
print("String com {} ", re.findall(padrao,string10))


