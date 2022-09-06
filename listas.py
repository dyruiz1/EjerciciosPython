
# listas: podemos almacenar varios datos en una sola referencia en memoria

nombres = ["juan", "juan", "sara", "samuel"]
#acceder a toda la lista
nombres.remove("juan")
print(nombres)

#acceder a una posicion o varias
#print(nombres[0], nombres[1])

# para recorrer el ciclo, por iteracion obtener cada uno de los datos, es como una variable auxiliar como si fuera un for each
# for nombre in nombres:
#     print(nombre)


# lista=[1,2,3,4,5]
#son entre corchetes

#RECORRER UNA LISTA
# for numero in lista:
#     print(numero)

# #APPEND 
# lista.append(100)
# print(lista)

# #INSERT
# lista.insert(2,200)
# print(lista)

#BUSCAR UN INDICE
#print(list(e for e in list_ejem if e['name']  == 'Juan')[0])

#INSERTAR UH ELEMENTO EN UN INDICE ESPECÍFICO
# nombres.insert(3, "ana")
# # si ya la posicion esta ocupada corre al que este ocupando la posicion


# #MOSTRAR EL TAMAÑO DE LA LISTA
# print(len(nombres))


# #REMOVER EL ELEMENTO
# nombres.remove("juan")
# print(nombres)
#si hay dos nombres iguales, elimina solo uno


#REMOVER ELEMENTO POR INDICE
# del nombres[1]

# #LIMPIAR LISTA
# nombres.clear()


