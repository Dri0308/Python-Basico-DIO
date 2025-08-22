#print("Hello, World!")
nome = "adriana"
print(nome.title())#Com este método, apenas a primeira letra de cada palavra é maiúscula.

nome = "Adriana Rocha"
print(nome.lstrip(" "))
print(nome.rstrip())

materias_da_semana = ["Python", "Banco de Dados", "Github", "Ingles"]
print(materias_da_semana[3])
print(materias_da_semana[-2])
print(materias_da_semana[ 2:4])

lista = [1,2,3,4,8]
for indice, lista in enumerate(lista):
    print({indice}, {lista})

lista = [0,2,4,6]
lista.reverse()
print(lista)

lista = ["Hyunjin", "Seungmin", "Changbin", "Felix", "Han", "Lee Know", "I.N", "Bang Chan"]
lista.sort(key=lambda x: len(x))
print(len(lista))

danceracha = ("Lee Know", "Hyunjin", "Felix",)
print(len(danceracha))
print(danceracha.count("Hyunjin"))
print(danceracha.index("Felix"))