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

SKZ_Members = ["Changbin", "Felix", "Hunjin", "I.N", "Bang Chan", "Lee Know", "Seungmin", "Han"]
for indice, SKZ_Members in enumerate(SKZ_Members):
    print(f'{indice} : {SKZ_Members}')