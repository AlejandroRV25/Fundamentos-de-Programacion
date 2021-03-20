# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:17:17 2021

@author: juana
"""
contador_rep=0
suma=0
contador_est=0
promedio=0
n=int(input("Ingrese la cantidad: "))
for f in range(n):
    e=int(input("Ingrese su edad: "))
    suma=suma+e
    contador_est=contador_est+1
    promedio=suma/n
    
contador_rep=contador_rep+1
print("El promedio es: ",promedio)    
    