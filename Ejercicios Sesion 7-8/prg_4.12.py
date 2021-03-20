# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:03:11 2021

@author: juana
"""

contador_rep=0
while contador_rep < 1:
    print("""
          1.Sumar
          2.Multiplicar
          3.Dividir
          """) 
    
    
    opcion=int(input("Ingrese el numero de la operación que desea realizar: "))
    a=float(input("Ingrese el primer valor: "))
    b=float(input("Ingrese el segundo valor: "))
    suma= a+b
    multiplicacion=a*b
    division= a/b
    
    if opcion == 1:
        print("La suma de los valores es: ",suma)
    elif opcion == 2:
        print("La multiplicacion de los valores es: ",multiplicacion)
    elif opcion == 3:
        print("La division de los valores es: ",division)
    else:
        print("Escoja una opcion correcta")
        
    contador_rep=contador_rep+1    