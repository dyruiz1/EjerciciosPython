 
print("***MENU***")
print("1. Agregar 1 empanada")
print("2. Mostrar Empanada")
print("3. Eliminar Empanada")
print("4. Buscar Empanada")
print("5. SALIR")
opcion=100
#DATOS EMPANADA
#Sabor
#Ingredientes (x3)
#Precio Fabircación
#Precio venta


empanadas=[]

while(opcion!=5):
    empanada={}
    opcion =int(input("Digite una opcion: "))
    if(opcion==1):
        empanada['sabor']=input("digite su sabor: ")
        empanada['ingredientes']=[]
        for i in range(3):
            
            empanada['ingredientes'].append(input("Digita el nombre del ingrediente: "))
        
        empanada['precioFabricacion']=input("digite precio de fabricacion: ")
        empanada['precioVenta']=input("digite precio de venta: ")
        empanadas.append(empanada)
        print("agregando empanadas")
    elif(opcion==2):
        
        print(empanadas)
        print("Mostrando empanadas")
    elif(opcion==3):
        sabor = input("Digite el sabor que desea eliminar: ")
        index=[x['sabor'] for x in empanadas].index(sabor)
        empanadas.pop(index)
        print(empanadas)
    elif(opcion==4):
        sabor = input("Digite el sabor que desea buscar: ")
        empanada= list(e for e in empanadas if e['sabor']  == sabor)       
        if(len(empanada) > 0):
            print(empanada[0])
        else:
            print("no se encuentra la empanada")
    else:
        print("digite una opcion valida")
else:
    print("fin")

    
    