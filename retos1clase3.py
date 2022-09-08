#1.un programa que reciba y sume numeros mientras sean positivos
# def main():
#     print("SUMA DE NÚMEROS")
#     numero = int(input("Escriba un número: "))
#     suma = 0
#     while numero >= 0:
#         suma += numero
#         #suma a la variable del lado izquiero el valor del lado derecho, es decir comienza en cero y va sumando
#         numero = int(input("Escriba otro número: "))
#     print()
#     print(f"La suma de los números positivos introducidos es {suma}.")


# if __name__ == "__main__":
#     main()


#2. codificar un programa que presente un menu de 4 opciones y reciba un numero natural para realizar las siguientes operaciones 

    # 0: salida
    # 1: encuentre si el numero es multiplo de 2
    # 2: encuentre la raiz cuadrada del numero
    # 3: sume 100 al numero ingresado
    # 4: eleve a la 2 el numero ingresado   

    # from cmath import sqrt
    # import math

    # observador = 100
    # print("** MENU**")
    # print("0. SALIR")
    # print("1. Decir si es o no múltiplo de 2")
    # print("2. la raiz cuadrada del número")
    # print("3. sumar 100 al número ingresado")
    # print("4. elevar a la 2 el número ingresado")

    # while(observador != 0):
    #     observador = int(input("digite una opcion: "))
    #     if(observador == 0):
    #         print("chao")
    #         break
    #     elif(observador == 1):
    #         numero = int(input("ingrese un número: "))
    #         if(numero % 2 ==0):
    #             print(f'el numero {numero} es múltiplo de 2')
    #         else:
    #             print(f'el numero {numero} no es múltiplo de 2')
    #     elif(observador ==2):
    #         numero = int(input("ingrese un número: "))
    #         print(f'la raiz cuadrad del numero {numero} es: ')
    #         print(math.sqrt(numero)) 
    #     elif(observador ==3):
    #         numero = int(input("ingrese un número: "))
    #         print(f'el numero  {numero} + 100  es: ')
    #         print(numero + 100)
    #     elif(observador ==4):
    #         numero = int(input("ingrese un número: "))
    #         print(f'el numero {numero} elevado al cuadrado es: ')
    #         print(math.pow(numero, 2)) 
    #     else:
    #         print(f'Digita una opcion valida')
    # else: 
    #     print("termine")


#3. Mostrar los números del 1 al 200 saltando de 12 en 12(1,12,24…)

    # for observador in range(0,200,12):
    #     print(observador)



#4. Pedir 20 números y contar cuantos de los ingresados fueron negativos, neutros y positivos
# x=1
# a=0
# b=0
# c=0

# while(x<=10):
#     n = int(input(f"ingresa el numero {x}:"))
#     if(n==0):
#         a = a + 1
#     elif(n < 0):
#         b = b + 1
#     else:
#         c = c + 1
#     x += 1
# print (f"{a} numeros neutros")
# print (f"{b} numeros negativos")
# print (f"{c} numeros positivos")