#crear menu con tres opciones:
#1. Opcion 1:Temperaturas
#2. Opcion 2:Datos de Personas
#3. Opcion 3:Salir


import os

def Temperaturas():                     #Definicion de Funcion
    print("******TEMPERATURAS******")
    #Ingresar n temperaturas donde n es un numero ingresado por teclado
    #Mostrar el promedio de las temperaturas ingresadas
    suma=0
    veces=int (input("Cuantas temperaturas necesita ingresar?"))
    for x in range(veces):
        tempe=float(input("Digite una temperatura: "))
        suma=suma+tempe

    print("El promedio de las temperaturas ingresdas es: " ,round((suma/veces),2  ))

    pausa=input("Presione una tecla para continuar")

def Personas():
    print("****** DATOS DE PERSONAS ******")

    pausa=input("Presione una tecla para continuar")


seguir=True
while seguir:
    os.system('cls')
    print ("1. Temperaturas")
    print ("2. Datos de personas")
    print ("3. Salir")
    op=int(input("Ingrese opcion 1,2,3"))
    if(op==1):
        Temperaturas()        #invocar o llamar a una funcion
    
    elif(op==2):
        Personas()
    
    else:
        print ("Finalizar")
        break