# tupla=(1,2,3,4,5)
# #son entre parentesis
# print(tupla)

# for numero in tupla:
#     print(numero)

# #tupla.append(100)
# #print(tupla)

# #transformando una tupla en una lista
# lista=list(tupla)
# print(lista)

# #lista en tupla
# mylist = list((1,2,3,4))
# mytuple = tuple(mylist)
# print(mytuple)


# a = [1, 2, 3]
# a = tuple(a)

# (1, 2, 3)
# a = list(a)
 

#convertir la tupla = (50,45,20,30,40,87) en una lista que solo contenga numeros> 40


# tupla=(50,45,20,30,40,87)
# lista=list(tupla)
# lista.sort()
# print(lista)
# filter = filter(lambda item: item > 40, lista)
# filteredList = list(filter)
# print(filteredList)


#convertir la tupl = (50,45,20,30,40,87 ) en un alista que solo contenga numeros pares
mytupla=(50,45,20,30,40,87)
lista=list(mytupla)
lista.sort()
print(lista)
filter = filter(lambda item: item % 2 == 0, lista)
filteredList = list(filter)
print(filteredList)
