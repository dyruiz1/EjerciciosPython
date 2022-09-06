
lista=[1,2,3,4,5]
#son entre corchetes

#Recorrer un lista
for numero in lista:
    print(numero)

#APPEND 
lista.append(100)
print(lista)

#INSERT
lista.insert(2,200)
print(lista)

#BUSCAR UN INDICE
#print(list(e for e in list_ejem if e['name']  == 'Juan')[0])





# Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7

# arraylength= int(input("Digite el largo del array: "))
# arraynumero = []

# for i in range(1, arraylength+1):
#   arraynumero.append(i * 7)

# print (f"{arraynumero} lista de números multiplos de 7")



#Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario


# arraylength= int(input("Digite el largo del array: "))
# arraynumero = []

# for i in range(0, arraylength):
#   num = int(input("Digite un número: "))
#   arraynumero.append(num)

# print (f"{arraynumero} lista de números")



#Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados

# ciudades = []

# for i in range(0, 7):
#   ciudad = input("Digite el nombre de una ciudad: ")
#   ciudades.append(ciudad)

# ciudades.reverse()
# print (f"{ciudades} lista de ciudades")



#Leer 20 números enteros y guardar en una lista, después permitir que el usuario 
# busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso


arraynumero = []

for i in range(0, 20):
  num = int(input("Digite un número: "))
  arraynumero.append(num)

numero_buscado = int(input("Digite el numero que desea buscar: "))
if(numero_buscado in arraynumero):
  print (f"{numero_buscado} si está en la lista ")
else:
  print (f"{numero_buscado} no está en la lista ")
  
