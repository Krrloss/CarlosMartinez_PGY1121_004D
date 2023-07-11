import os
import numpy as np
ganancias= 0
compradep= 0
gantot= 0
rutma= np.empty([10], type(int))
def llenarMatriz(depto,rut):
    p=1
    for i in range(10):
        for j in range(4):
            depto[i,j]=p
            p+=1
            mostrarDisponibles(depto)
            if(p==2):
                os.system("cls")
                print("ingresando rut ")
                rut=int(input("Ingrese su rut, debe tener más de 8 caracteres: "))
                for i in range(10):
                    rutma=+rut
                p=+1
                if(rut)>9:
                    break
                else:
                    print("deben ser entre 8 y 9 caracteres")
            if(p==3):
                deptocom=input("ingrese el departamento a comprar")
            if deptocom==[i,j]:
                compradep=deptocom+[i,j] 
                
                print("departamento elegido es: ",compradep)
def listado(list):
    os.system("cls")
    print(rutma)
def gananciastot(ganancias):
    os.system("cls")
    gantot=compradep+ganancias
    print("las ganancias totales son: ",gantot)

def mostrarDisponibles(depto):
    os.system("cls")
    for i in range(10):
        print("\n") #salto de linea
        for j in range(4):
            if(j==1):
                print("\t",depto[i,j], end="        ")
            else:
                print("\t",depto[i,j], end="    ")
    print("\n\n")
def validadept():
    dept=0
    while True:
        try: 
            dept=int(input("Ingrese número de asiento 1-40: "))
            if (dept>=1 and dept<=40):
                break
            else:
                print(" Error.. ingrese asiento entre  1 y 40")
        except ValueError:
            print(" Error.. ingrese asiento entre  1 y 40")
    return dept
def comprar(depto, tipo):
    for x in range(10):
        for i in range(4):
            if (depto[x,i]==tipo):
                depto[x,i]=0          #el depto esta vendido
                if i==0 or i==3:
                    pago=5000
                elif i==1 or i==2:
                    pago=4000

def ingreso(bolsa1,inicio,fin):#tambien funciona como validar
    while(True):
        try:
            x=int(input(bolsa1))
            if(x>=inicio and x<=fin):
                break
            else:
                print("Debe estar en el rango "+str(inicio)+" a "+str(fin))
        except ValueError:
            print("Debe se un numero entero")
    return x
