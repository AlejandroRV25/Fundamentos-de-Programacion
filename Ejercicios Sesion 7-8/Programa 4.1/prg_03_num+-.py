# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:34:11 2021

@author: juana
"""
cant_n=int(input("Ingrese el numero de datos: "))
contador_neg=0
contador_pos=0
contador_rep=0
contador_0=0

while contador_rep < cant_n:
    n=float(input("Por favor ingrese un número: "))
    
    if n > 0:
        contador_pos=contador_pos+1
    
    elif n < 0:
        contador_neg=contador_neg+1
    else:
        contador_0=contador_0+1
        
    contador_rep=contador_rep+1
    
print("La cantidad de números positivos es: ",contador_pos)
print("La cantidad de números negativos es: ",contador_neg)    
print("La cantidad de ceros es: ",contador_0)    
        