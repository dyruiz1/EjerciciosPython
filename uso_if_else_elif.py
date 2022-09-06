#ENTRADAS DEL PROBLEMA
edad= int(input("Digitala edad que tiene: "))

#PROCESO DEL PROBLEMA
if(edad >=0 and edad <= 14):
    print(f' tu edad es {edad} eres un niño')
elif(edad >14 and edad <= 28):
    print(f' tu edad es {edad} eres un joven')
elif(edad >28 and edad <= 60):
    print(f'tu edad es {edad} eres un adulto')
elif(edad >60 and edad <= 120):
    print(f' tu edad es {edad} eres un adulto mayor')   
else:
    print(f'Digite una opción valida')


#ENTRADAS DEL PROBLEMA
mes= input("Digita el mes : ")

#PROCESO DEL PROBLEMA
if(mes =="enero" or mes == "febrero" or mes == "marzo"):
    print(f' es el mes de {mes} estas en la estacion invierno')
elif(mes == "abril" or mes == "mayo" or mes == "junio"):
    print(f' es el mes de {mes} estas en la estacion primavera')
elif(mes == "julio" or mes == "agosto" or mes == "septiembre"):
    print(f' es el mes de {mes} estas en la estacion verano')
elif(mes == "octubre" or mes == "noviembre" or mes== "diciembre"):
    print(f' es el mes de {mes} estas en la estacion otoño')   
else:
    print(f'Digite una opción valida')


#ENTRADAS DEL PROBLEMA
nivelAgua= int(input("Digita el nivel del agua de la presa: "))

#PROCESO DEL PROBLEMA
if(nivelAgua >=0 and nivelAgua < 20):
    print(f'el nivel del agua {nivelAgua} es muy bajo')
elif(nivelAgua >= 20 and nivelAgua < 400):
    print(f'el nivel del agua {nivelAgua} es optimo')
elif(nivelAgua >= 400):
    print(f'el nivel del agua {nivelAgua} es muy peligroso')
else:
    print(f'Digite una opción valida')


