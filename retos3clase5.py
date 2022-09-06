
#1.convertir la tupla = (50,45,20,30,40,87) en una lista que solo contenga numeros> 40


# tupla=(50,45,20,30,40,87)
# lista=list(tupla)
# lista.sort()
# print(lista)
# filter = filter(lambda item: item > 40, lista)
# filteredList = list(filter)
# print(filteredList)


#2.convertir la tupla = (50,45,20,30,40,87 ) en un alista que solo contenga numeros pares
mytupla=(50,45,20,30,40,87)
lista=list(mytupla)
lista.sort()
print(lista)
filter = filter(lambda item: item % 2 == 0, lista)
filteredList = list(filter)
print(filteredList)
