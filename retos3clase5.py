
#1.convertir la tupla = (50,45,20,30,40,87) en una lista que solo contenga numeros> 40


# tupla=(50,45,20,30,40,87)
# lista=list(tupla)
# #para ordenar la lista
# lista.sort()
# print(lista)
# #filtra los mayores d40 sin incluir
# filter = filter(lambda item: item > 40, lista)
# filteredList = list(filter)
# #imprime la nueva lista
# print(filteredList)


#2.convertir la tupla = (50,45,20,30,40,87 ) en una lista que solo contenga numeros pares
mytupla=(50,45,20,30,40,87)
#la convierte en lista
lista=list(mytupla)
#la ordena
lista.sort()
print(lista)
#filtra los numeros pares
filter = filter(lambda item: item % 2 == 0, lista)
filteredList = list(filter)
print(filteredList)
