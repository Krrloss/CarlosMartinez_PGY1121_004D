import os
import numpy as np
import lib as lc
depto= np.empty([10,4], type(str))
lc.llenarMatriz(depto)
op = 0
l=0
while(op!=4):
        print("*********Casa Feliz***********")
        print("******************************")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. listado de compradores")
        print("4. ganancias totales")
        print("5. Salir")
        op=lc.ingreso("Elija opcion: ",1,5)
        if (op==1):
            lc.llenarMatriz(depto)
            input("<<Enter>> para continuar")
        if (op==2):
            if(l==1):
                lc.mostrarDisponibles(depto)
                os.system("pause")
        if (op==3):
            if(l==1):
                lc.listado
            else:
                os.system("cls")
                print("**************************************************")
                print("debe ingresar los datos antes de ver el mas votado")
                input("<<Enter>> para continuar")
                print("**************************************************")
        if (op==4):
            if(l==1):
                lc.gananciastot
            else:
                os.system("cls")
                print("**************************************************")
                print("debe ingresar los datos antes de ver el mas votado")
                input("<<Enter>> para continuar")
                print("**************************************************")
        if (op==5):
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break
        
