# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:43:44 2021

@author: juana
"""
contador_rep=0
while contador_rep < 1:
    
      print("""
      1.Sumar
      2.Restar
      3.Multiplicar
      4.Dividir
      """)
      
      opcion=int(input("Ingrese el numero de la operación que desea hacer: "))
      a=float(input("Ingrese el primer valor: "))
      b=float(input("Ingrese el segundo valor: "))
      suma= a+b
      resta= a-b
      multiplicacion=a*b
      division=a/b
     
      if opcion == 1:
          print("La suma de los 2 valores es: ",suma)
      
      elif opcion == 2:
          print("La resta de los 2 valores es: ",resta)
         
      elif opcion == 3:
          print("La multiplicacion de los 2 valores es: ",multiplicacion)
          
      elif opcion == 4:
          print("La division de los 2 valores es: ",division)
          
          
      contador_rep=contador_rep+1    